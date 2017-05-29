'''
Created on 2017/5/16

@author: Administrator
'''

import user
import connection

def change_head(img, username):
    url = "/static/user_head/"+username+".png"
    dist_url = "/HyrComputerVisionServer/HyrComputerVisionServer/HyrComputerVision/static/user_head/"+username+".png"
    import os
    dist_url = os.getcwd().replace('\\','/')+dist_url
    f = open(dist_url, "wb")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    conn = connection.conn
    cursor = conn.cursor()
    user.update_head(cursor, username, url)
    cursor.close()

def init_data_request(username):
    conn = connection.conn
    cursor = conn.cursor()
    res = user.search_by_username(cursor, username)
    if res['head_url'] == None:
        res['head_url'] = "/static/user_head/default_head.png"
        
    cursor.close()
    return res

def change_user_info(username, password, email):
    conn = connection.conn
    cursor = conn.cursor()
    user.update_password_email(cursor, username, password, email)
    cursor.close()