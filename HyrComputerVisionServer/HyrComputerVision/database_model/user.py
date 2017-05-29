#coding:utf-8
'''
Created on 2017/5/14

@author: Administrator
'''
import time
from time import sleep

'''
This is used for doing data exchange with database's table User
'''
    
def add(cursor, username, password, email):
    registered_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    SQL = r'insert into user (username, password, email, registered_time) values' + r'(' +'\''+username+ '\''+ "," +'\''+ password + '\''+ "," +'\''+ email +'\''+"," + '\'' + registered_time + '\'' +r')'
    cursor.execute(SQL)    
    return 1
    
def search_by_username(cursor, username):
    sleep(0.5)#恶意睡眠
    SQL = r"SELECT * FROM user WHERE username = '%s'" %username
    cursor.execute(SQL)
    res_list = cursor.fetchone()
     
    if res_list == None:
        return 0
    res_dict = {'username' : res_list[0], 'password':res_list[1], 'email': res_list[2], \
                'registered_time' : res_list[3], 'head_url':res_list[4]}
    return res_dict

def search_by_eamil(cursor, email):
    SQL = r"SELECT * FROM user WHERE email= '%s'" %email
    cursor.execute(SQL)
    res_list = cursor.fetchone()
    if res_list == None:
        return 0
    res_dict = {'username' : res_list[0], 'password':res_list[1], 'email': res_list[2], \
                'registered_time' : res_list[3], 'head_url':res_list[4]}
    return res_dict

def update_head(cursor, username, url):
    SQL = r"UPDATE user SET head_url='%s' WHERE username = '%s'" %(url,username)
    cursor.execute(SQL)
    
def update_password_email(cursor, username, password, email):
    SQL = r"UPDATE user SET password='%s' WHERE username = '%s'" %(password, username)
    cursor.execute(SQL)
    SQL = r"UPDATE user SET email='%s' WHERE username = '%s'" %(email, username)
    cursor.execute(SQL)
    
def exist_username(cursor, usename):
    return search_by_username(cursor, usename) != 0
    
def exist_email(cursor, email):
    return search_by_eamil(cursor, email) != 0