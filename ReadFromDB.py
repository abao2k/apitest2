__author__ = 'abao2k'
import sqlite3 as db

conn = db.connect('/Users/abao2k/Documents/python接口测试/web/interface/db.sqlite3',check_same_thread=False)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象


def db_get_cursor(sql):
    cursor = conn.execute(sql)
    return cursor

