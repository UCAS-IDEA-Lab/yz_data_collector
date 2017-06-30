#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sys
# sys.path.append('/root/workspace/yz_data_collector/agent')

import random
import datetime
import json
import os
import time
from optparse import OptionParser

from yz_agent.settings import data_path

PROVIDERIDs = ['STO', 'YTO', 'ZTO', 'BEST', 'YUNDA']
CITYCODEs = ['BJ', 'NJ', 'LZ', 'SZ', 'SH', 'GZ', 'FJ', 'NN']
COUNTRYCODEs = ['China', 'USA', 'Japan', 'Korea']
NAMEs = ['Alice', 'Bob', 'Crystal', 'Doc', 'Emma']
ADDRESSes = ['Road A', 'Road B', 'Road C', 'Road D']
CONTENTTYPEs = ['Food', 'Other']
CONTENTNAMEs = ['Goods1', 'Goods2', 'Goods3', 'Goods4', 'Goods5', 'Goods6']
DATE = None

FACILITYNAMEs = ['Station1', 'Station2', 'Station3', 'Station4', 'Station5', 'Station6']

DATA_TYPE = {
    'ErrorHandle': '00',
    'ExpressContract': '01',
    'ExpressContractState': '02'
}

def _get_exp():
    global DATE
    return {
        'info': {
            'logisticproviderid': random.choice(PROVIDERIDs),
            'mailno': str(random.randint(1000000, 9999999)),
            "mailtype": str(random.randint(1, 4)),
            "weight": str(random.randint(1, 40)),
            'sencitycode': random.choice(CITYCODEs),
            'reccitycode': random.choice(CITYCODEs),
            'senareacode': random.choice(COUNTRYCODEs),
            'recareacode': random.choice(COUNTRYCODEs),
            'inserttime': time.time()
        },
        'send': {
            'senname': random.choice(NAMEs),
            'senmobile': '13' + str(random.randint(715839205, 979989299)),
            'senphone': '86' + str(random.randint(2301086, 86908090)),
            "senprov": str(random.randint(1, 40)),
            "sencity": str(random.randint(1, 40)),
            "sencounty": str(random.randint(1, 40)),
            'senaddress': random.choice(ADDRESSes)
        },
        'recv': {
            'recname': random.choice(NAMEs),
            'recmobile': '13' + str(random.randint(715839205, 979989299)),
            'recphone': '86' + str(random.randint(2301086, 86908090)),
            "recprov": str(random.randint(1, 40)),
            "reccity": str(random.randint(1, 40)),
            "reccounty": str(random.randint(1, 40)),
            'recaddress': random.choice(ADDRESSes)
        },
        'pkg': {
            'typeofcontents': random.choice(CONTENTTYPEs),
            'nameofcoutents': random.choice(CONTENTNAMEs),
            'mailcode': random.choice(['Y', 'N']),
            'recdatetime': DATE,
            'insurancevalue': str(random.randint(100, 400))
        }
    }

def _get_exp_state():
    return {
        'info': {
            'logisticproviderid': random.choice(PROVIDERIDs),
            'mailno': str(random.randint(1000000, 9999999))
        },
        'state': {
            'time': time.time(), 
            'desc': '揽收转发',
            'city': random.choice(CITYCODEs),
            "facilitytype": str(random.randint(1, 2)),
            "facilityno": str(random.randint(1, 40)),
            "facilityname": random.choice(FACILITYNAMEs),
            'action': str(random.randint(1, 40)),
        },
        'contact': {
            'contacter': random.choice(NAMEs),
            'contactphone': '13' + str(random.randint(715839205, 979989299)),
        }
    }

DATA = {
    'ExpressContract': _get_exp,
    'ExpressContractState': _get_exp_state
}

def _check_and_create(date, datatype):
    
    def get_file_no(arg, dirname, filelist):
        for filename in filelist:
            # Get the biggest file name
            # Check if this file's line number
            if int(filename) > arg[0]:
                arg[0] = int(filename)
                with open('/'.join([dirname, filename]), 'rb') as fd:
                    while fd.readline() != '':
                        arg[1] += 1

    HOME = '/'.join([data_path, date, datatype])
    no = [0, 0]
    if not os.path.exists(HOME):
        os.makedirs(HOME)
    else:
        os.path.walk(HOME, get_file_no, no)

    return '%05d' % no[0], no[1]

def _gen_data(file_name, line_no, opt):
    global DATE
    date = opt.date
    while True:
        file_now = '/'.join([data_path, date, DATA_TYPE[opt.datatype], file_name])
        print 'Writing data to %s...' % file_now
        with open(file_now, 'ab+') as fd:
            while line_no < opt.max:
                data = DATA[opt.datatype]()
                fd.write(json.dumps(data) + '\n')
                line_no += 1
            fd.write('END\n')

        date = datetime.datetime.now().strftime('%Y/%m/%d')
        if date != opt.date:
            file_name, line_no = _check_and_create(date, DATA_TYPE[options.datatype])
            DATE = date
        else:
            file_name = "%05d" % (int(file_name)+1)
            line_no = 0

def main():
    usage = 'Usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-d', '--date', dest='date', \
            default=datetime.datetime.now().strftime('%Y/%m/%d'), \
            help="The date of data to be generated(e.g. 2017/06/12), \
            default is today")
    parser.add_option('-t', '--type', dest='datatype', \
            default='ExpressContract', \
            choices=['ErrorHandle', 'ExpressContract', 'ExpressContractState'], \
            help="The type of data to generated")
    parser.add_option('-m', '--max', dest='max', \
            default=100000, \
            help="The max line in a data file")
    options, args = parser.parse_args()

    file_name, line_no = _check_and_create(options.date, DATA_TYPE[options.datatype])

    global DATE
    DATE = options.date
    _gen_data(file_name, line_no, options)

if __name__ == '__main__':
    main()

