# -*- coding: utf-8 -*-

import json
import MySQLdb
import logging
import eventlet
from eventlet.green import urllib2

LOG = logging.getLogger()

from settings import mysql_addr, mysql_port, mysql_user, \
        mysql_pwd, mysql_db, agent_api_port
import remote_call

class AgentView(object):

    def __init__(self):
        self.db = MySQLdb.connect(host=mysql_addr, port=mysql_port, user=mysql_user, \
                passwd=mysql_pwd, db=mysql_db)
        self._agent_list = {}
        self._pool = eventlet.GreenPool(size=256)
        self._agent_status = ['off_line', 'on_line && working', 'on_line && sleeping']
        self._agent_action = {
            'start': remote_call.agent_start,
            'stop': remote_call.agent_stop,
            'speedup': remote_call.agent_speedup,
            'slowdown': remote_call.agent_slowdown
        }

        self._initial_agent_list()

    def _initial_agent_list(self):
        cur = self.db.cursor()
        sql = "select id, addr from agent_manager where status!=0"
        cur.execute(sql)
        for row in cur.fetchall():
            self._agent_list[row[0]] = row[1]
        LOG.debug("Agent list: %s", self._agent_list)

    def register_agent(self, info):
        """
        :param info: {'id':, 'addr':}
        """
        if self._agent_list.has_key(info.id):
            return {
                'success': False,
                'reason': "Agent %s already existed." % info.id
            }

        cur = self.db.cursor()
        re = cur.execute("select id from agent_manager where id='%s'" % info.id)
        if re == 0:
            sql = "insert into agent_manager(id, addr, status) values ('%s', '%s', 1)" \
                    % (info.id, info.addr)
            cur.execute(sql)
        else:
            sql = "update agent_manager set addr='%s', status=%d where id='%s'" \
                    % (info.addr, 1, info.id)
            cur.execute(sql)
        self.db.commit()
        self._agent_list[info.id] = info.addr
        return {'success': True}

    def unregister_agent(self, agent_id):
        if not self._agent_list.has_key(agent_id):
            return {
                'success': False,
                'reason': 'Agent %s was not registered.' % agent_id
            }

        cur = self.db.cursor()
        re = cur.execute("delete from agent_manager where id='%s'" % agent_id)
        self.db.commit()
        del self._agent_list[agent_id]
        return {'success': True}

    def ping_agents(self):

        def __ping(args):
            try:
                re = urllib2.urlopen(args[1]).read()
                return {
                    'success': True,
                    'id': args[0],
                    'info': re
                }
            except Exception, e:
                LOG.error(e)
                return {
                    'success': False,
                    'id': args[0],
                    'info': e
                }
        
        addrs = [(k, "http://%s:%s/api/ping" % (v, agent_api_port)) \
                for k, v in self._agent_list.items()]
        cur = self.db.cursor()
        for ret in self._pool.imap(__ping, addrs):
            LOG.debug(ret)
            if not ret['success']:
                self.unregister_agent(ret['id'])

            info = json.loads(ret['info'])
            sql = "update agent_manager set volume=%f, status=%d where id='%s'" \
                    % (info['volume'], info['status'], ret['id'])
            LOG.debug(sql)
            r = cur.execute(sql)
            LOG.debug('%d row affected.' % r)
        self.db.commit()

    def list_agents(self):
        cur = self.db.cursor()
        cur.execute("select id from agent_manager")
        rets = cur.fetchall()
        return [row[0] for row in rets]

    def show_agent(self, agent_id):
        cur = self.db.cursor()
        cur.execute("select * from agent_manager where id='%s'" % agent_id)
        ret = cur.fetchone()
        return (ret[0], ret[1], self._agent_status[ret[2]], \
                ret[3].strftime('%b-%d-%y %H:%M:%S'), '%f KB/s' % ret[4])

    def agent_action(self, agent_id, action):
        cur = self.db.cursor()
        cur.execute("select addr from agent_manager where id='%s'" % agent_id)
        return self._agent_action[action](cur.fetchone()[0])

agent_view = AgentView()

