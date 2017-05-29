#coding:utf-8
'''
Created on 2017/5/17

@author: Administrator
'''
import time
import datetime
import connection

product_table = ["emotion", "obj", "face", "carPlate"]
type_table = ["free", "standard"]

import random, string
 
def get_random_key(random_length=30):
    chars = list(string.ascii_letters+string.digits)
    return ''.join([random.choice(chars) for i in range(random_length)])

def add_buy_product_record(username, product, type):
    '''
    product:
        0 表情识别
        1 物品识别
        2 人脸识别
        3 车牌识别
    type:
        0 免费
        1 标准
    '''
    key = get_random_key(30)
    left_times = {0:"100",1:"NULL"}[type];
    cur_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    end_time = (datetime.date.today() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    
    SQL = "INSERT INTO user_product (username, product, start_time, end_time,\
     product_key, left_times, type) VALUES ('%s','%s','%s','%s', '%s','%s', '%s')"%(username, product_table[product],\
                                            cur_time, end_time, key, left_times, type_table[type])
    conn = connection.conn
    cursor = conn.cursor()
    cursor.execute(SQL)
    cursor.close()

def remove_product_record():
    '''
                这个函数在每天24点触发清理过期的产品
    '''
    pass

def decrease_left_time(product_key):
    '''
                 免费用户每使用一次触发，用来减少使用次数
    '''
    pass

def search_by_username(username):
    '''
                用户名搜索记录，用来个人账户初始化
    '''
    SQL = "SELECT * FROM user_product WHERE username = '%s'"%username
    conn = connection.conn
    cursor = conn.cursor()
    cursor.execute(SQL)
    res_lists = list(cursor.fetchall())
    res_dict = []
    keys_name = ["username", "product", "start_time", "end_time", "product_key", "left_times", "type"]
    for row in res_lists:
        record = dict(zip(keys_name, row))
        record["start_time"] = record["start_time"].strftime("%Y-%m-%d")
        record["end_time"] = record["end_time"].strftime("%Y-%m-%d")
        res_dict.append(record)
    cursor.close()
    return res_dict
    
def is_exist(username, product, type):
    '''
                 判断数据库是否存在重复购买记录
    '''
    
    SQL = "SELECT * FROM user_product WHERE username = '%s' AND\
     product = '%s' AND type = '%s'" %(username, product_table[product], type_table[type])
    conn = connection.conn
    cursor = conn.cursor()
    cursor.execute(SQL)
    res = (len(cursor.fetchall()) != 0)
    cursor.close()
    
    return res

    
    