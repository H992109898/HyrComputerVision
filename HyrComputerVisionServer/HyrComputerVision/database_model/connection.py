'''
Created on 2017/5/14/

@author: Administrator
'''


import MySQLdb
conn = MySQLdb.Connect(host = '127.0.0.1',
                           user = 'root',
                           passwd = 'root',
                           port = 3306,
                           db = 'hyr_computer_vision',
                           charset = 'utf8')
conn.autocommit(False)
