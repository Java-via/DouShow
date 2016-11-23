# _*_ coding: utf-8 _*_

import pymysql


def db_conf():
    conn = pymysql.connect(host="54.169.79.230", db="db_doumovies", user="appuser", passwd="123", charset="utf8")
    cur = conn.cursor()
    return conn, cur
