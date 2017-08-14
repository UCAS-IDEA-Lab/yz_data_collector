#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script is used for inserting data to MySQL.
# You need pre-install MySQLdb-python lib for using this script.

from data_gen import DATA

import MySQLdb
import sys
from optparse import OptionParser

def _construct_exp():
    def __con():
        src_data = DATA['ExpressContract']()
        return (src_data['info']['logisticproviderid'], \
                src_data['info']['mailno'], \
                src_data['info']['mailtype'], \
                src_data['info']['weight'], \
                src_data['info']['sencitycode'], \
                src_data['info']['reccitycode'], \
                src_data['info']['senareacode'], \
                src_data['info']['recareacode'], \
                src_data['send']['senname'], \
                src_data['send']['senmobile'], \
                src_data['send']['senphone'], \
                src_data['send']['senprov'], \
                src_data['send']['sencity'], \
                src_data['send']['sencounty'], \
                src_data['send']['senaddress'], \
                src_data['recv']['recname'], \
                src_data['recv']['recmobile'], \
                src_data['recv']['recphone'], \
                src_data['recv']['recprov'], \
                src_data['recv']['reccity'], \
                src_data['recv']['reccounty'], \
                src_data['recv']['recaddress'], \
                src_data['pkg']['typeofcontents'], \
                src_data['pkg']['nameofcoutents'], \
                src_data['pkg']['mailcode'], \
                src_data['pkg']['recdatetime'], \
                src_data['pkg']['insurancevalue'], \
                src_data['info']['inserttime'])

    sql = """insert into ExpressContract(logisticproviderid, 
             mailno, mailtype, weight, sencitycode, reccitycode, senareacode, 
             recareacode, senname, senmobile, senphone, senprov, sencity, 
             sencounty, senaddress, recname, recmobile, recphone, recprov, reccity, 
             reccounty, recaddress, typeofcontents, nameofcoutents, mailcode, recdatetime, 
             insurancevalue, inserttime) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    return sql, __con

INSERT = {
    'ExpressContract': _construct_exp,
    'ExpressContractState': None
}

def _main(opt):
    db = MySQLdb.connect(host=opt.host, port=opt.port, user=opt.user, \
            passwd=opt.passwd, db=opt.database)
    cur = db.cursor()
    sql, con = INSERT[opt.table]()

    print 'Inserting data to %s' % opt.table

    for _ in xrange(opt.num):
        data = [con() for __ in xrange(opt.batch)]
        cur.executemany(sql, data)
        db.commit()
        print 'batch %d' % _

    print '%d records were inserted.' % (opt.batch*opt.num)

def main():
    usage = 'Usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-H', '--host', dest='host', \
            default='localhost', \
            help='The address of mysql server, default is localhost.')
    parser.add_option('-P', '--port', dest='port', \
            default=3306, \
            help='The port of mysql server, default is 3306.')
    parser.add_option('-u', '--user', dest='user', \
            default='root', \
            help="The user to login, default is root.")
    parser.add_option('-p', '--passwd', dest='passwd', \
            default='', \
            help="The password for user to login, default is none.")
    parser.add_option('-d', '--database', dest='database', \
            default='yz', \
            help="The database to access, default is yz.")
    parser.add_option('-t', '--table', dest='table', \
            default='ExpressContract', \
            choices=['ExpressContract', 'ExpressContractState'], \
            help="The table of data to generated")
    parser.add_option('-b', '--batch', dest='batch', \
            default=10000, \
            help='The batch size of data to insert, default is 10000.')
    parser.add_option('-n', '--num', dest='num', \
            default=10000, \
            help='The number of batch to insert, default is 10000.')
    options, args = parser.parse_args()

    try:
        _main(options)
    except Exception, e:
        print e
        sys.exit(1)

if __name__ == '__main__':
    main()

