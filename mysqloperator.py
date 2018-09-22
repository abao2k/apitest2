__author__ = 'abao2k'
import pymysql.cursors
from testdata.getpath import GetConfig
import configparser

config  = configparser.ConfigParser()
config.read(GetConfig('dbconfig.conf'))
db='TESTDB'
host = config[db]['host']
user = config[db]['user']
password = config[db]['password']
db_name = config[db]['db']
charset = config[db]['charset']

'''
host ="127.0.0.1"
user = "root"
password ="123456"
db = "polls"
'''


class MySQLcaozuo():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()


    def insert(self, table_name, data):
        for key in data:
            data[key] = "'"+str(data[key])+"'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value +")"
        #print("real_sql=="+real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def update(self, table_name, setsql ,wheresql):
        real_sql = "update " + table_name + " set " + setsql + " where  " + wheresql
        #print("real_sql=="+real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def select(self, table_name, selectsql ,wheresql):
        real_sql = "select  "+selectsql+" from  " + table_name +  " where  " + wheresql
        #print("real_sql=="+real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            rs = cursor.fetchone()
            #print (rs['votes'])
            return rs['votes']



    def delete(self, table_name, wheresql):
        real_sql = "delete from  " + table_name + "  where  " + wheresql
        #print("real_sql=="+real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db = MySQLcaozuo()
    table_name = "polls_choice"
    selectsql = " votes "
    wheresql = "id =2"
    a = db.select(table_name,selectsql,wheresql)
    print (a)
    db.close()

    '''
    table_name = "poll_question"
    data = {'id':1, 'question_text':'你喜欢的游戏是什么?'}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
    '''