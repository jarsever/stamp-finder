#!/usr/bin/env python

import argparse, curses, sys, os, logging, time, traceback
from src.process import Process
from datetime import datetime, timedelta




'''---------------------------- P_args() ------------------------------+
|                                                                      |
|  This function will parse all of the arguments and return a          |
|  dictionary that will then be sent to the Data() class.              |
|                                                                      |
|  This function will call convert_date() for some of the arguments.   |
|                                                                      |
+--------------------------------------------------------------------'''

def P_args(help=False):
    parser = argparse.ArgumentParser(description='Stamp-Finder Tool v0.1.0')

    parser.add_argument('-q',
        help="Run 'Quick' version skipping the hashes.",
        default=False,
        action='store_true')

    parser.add_argument('-E',
        help="Epoch or Beginning of time. 'YYYY,MM,DD'",
        default='1970,1,1,0,0,0')

    parser.add_argument('-s',
        help="Start Date. Defaults to one(1) week ago. 'YYYY,MM,DD,HH,mm,ss'",
        default=datetime.now()-timedelta(days=7))

    parser.add_argument('-e',
        help="End Date. Defaults to todays date.  'YYYY,MM,DD,HH,mm,ss'",
        default=datetime.now())

    parser.add_argument('-l',
        help="Process as 'Little Endian'. Defaults to 'Big Endian'.",
        default=False,
        action='store_true')

    parser.add_argument('-p',
        help='Path to FILE or DIR. It is reletive to the current directory. \
        Default is to process all files from current DIR.',
        default=os.getcwd())

    print ''
    return vars(parser.parse_args())



if __name__ == '__main__':
    try:
        s = time.time()
        logging.basicConfig(filename='{0}/sfinder.log'.format(os.path.expanduser('~')),
            format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG,
            datefmt='%m/%d/%Y %H:%M:%S')

        Process(P_args())

        e = time.time()
        print '\n[INFO] Program Finished in: {0}\n'.format(timedelta(seconds=round(e-s)))

        logging.info('Processing Finished Sucessfully!!\n')
        sys.exit(0)
    except KeyboardInterrupt:
        print '\n\n[ERROR] Program terminated by User!\n'
        logging.error('Stamp-Finder was killed by User!\n')
    except Exception as e:
        print '\n[ERROR] {0}'.format(e)
        print 'Check ~/sfinder.log for more information. :(\n'
        logging.critical(e)
        logging.critical(traceback.format_exc())
        sys.exit(1)
