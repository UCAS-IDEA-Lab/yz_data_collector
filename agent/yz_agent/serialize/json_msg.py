# -*- coding: utf-8 -*-

import json

class MsgBody(object):
    _id = ''
    _data = ''
    _type = ''
    _usage = ''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, v):
        self._id = v

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, v):
        self._type = v

    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, v):
        self._usage = v

    def SerializeToString(self):
        return json.dumps({
            'id': self._id,
            'data': json.loads(self._data),
            'type': self._type,
            'usage': self._usage
        })

