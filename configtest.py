__author__ = 'abao2k'

import configparser

config  = configparser.ConfigParser()
config.read('dbconfig.conf')
db='TESTDB'
host = config[db]['host']
port = config[db]['port']
user = config[db]['user']
passwd = config[db]['passwd']
db_name = config[db]['db']
charset = config[db]['charset']