__author__ = 'abao2k'
from mysqloperator import MySQLcaozuo
def inster_data(table, datas):
    db = MySQLcaozuo()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

def updata_data(table, setsql,wheresql):
    db = MySQLcaozuo()
    db.update(table, setsql,wheresql)
    db.close()


def selete_one(table,selectsql,wheresql):
    db = MySQLcaozuo()
    rs = db.select(table,selectsql,wheresql)
    return rs
    db.close()

def delete_data(table,wheresql):
    db = MySQLcaozuo()
    db.delete(table,wheresql)
    db.close()



table_poll_question = "polls_question"
datas_poll_question =[ {'id': 1, 'question_text': '你最喜欢的电视？'},
                       {'id': 2, 'question_text': '你最喜欢吃的水果？'},
                        ]

table_poll_choice = "polls_choice"
datas_poll_choice =[{'id': 1, 'choice_text': '三国演义', 'votes': 0, 'question_id': 1},
                    {'id': 2, 'choice_text': '西游记', 'votes': 0, 'question_id': 1},
                    {'id': 3, 'choice_text': '红楼梦', 'votes': 0, 'question_id': 1},
                    {'id': 4, 'choice_text': '苹果', 'votes': 0, 'question_id': 2},
                    {'id': 5, 'choice_text': '香蕉', 'votes': 0, 'question_id': 2},
                    {'id': 6, 'choice_text': '西瓜', 'votes': 0, 'question_id': 3},
                    ]

def init_data():
    inster_data(table_poll_question, datas_poll_question)
    inster_data(table_poll_choice, datas_poll_choice)

def update():
    updata_data(table_poll_choice," votes = votes+1 "," id=1")

def selete():
    rs = selete_one(table_poll_choice," votes "," id=1")
    return rs

def delete():
    delete_data(table_poll_choice," id=1")

if __name__ == '__main__':
    init_data()