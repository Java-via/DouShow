# _*_ coding: utf-8 _*_

import pymysql


def db_conf():
    conn = pymysql.connect(host="localhost", db="db_doumovies", user="appuser", passwd="123", charset="utf8")
    cur = conn.cursor()
    return conn, cur
