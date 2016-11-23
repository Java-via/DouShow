# _*_ coding: utf-8 _*_

from z_db_conf import *
from z_db_sql import *


def year_2016_coutry():
    level_country = ["China", "USA", "Japan", "UK",
                     "France", "Korea", "Germany", "Italy",
                     "India", "Thailand", "Spain", "Canada",
                     "Australia", "Russia", "Iran", "Ireland",
                     "Sweden", "Brazil", "Denmark", "Poland",
                     "Czech Republic", "Argentina", "Belgium", "Mexico",
                     "New Zealand", "Netherlands", "Austria", "Turkey",
                     "Hungary", "Israel"]
    dict_level_country = {item: 0 for item in level_country}
    try:
        conn, cur = db_conf()
        cur.execute(SQL_COUNT_OF_COUNTRY)
        for name, score, country in cur.fetchall():
            if ("中国" in country) or ("中国大陆" in country) or ("香港" in country) or ("台湾" in country) or ("内地" in country):
                dict_level_country["China"] += 1
            if "美国" in country:
                dict_level_country["USA"] += 1
            if "日本" in country:
                dict_level_country["Japan"] += 1
            if "英国" in country:
                dict_level_country["UK"] += 1

            if "法国" in country:
                dict_level_country["France"] += 1
            if "韩国" in country:
                dict_level_country["Korea"] += 1
            if "德国" in country:
                dict_level_country["Germany"] += 1
            if "意大利" in country:
                dict_level_country["Italy"] += 1

            if "印度" in country:
                dict_level_country["India"] += 1
            if "泰国" in country:
                dict_level_country["Thailand"] += 1
            if "西班牙" in country:
                dict_level_country["Spain"] += 1
            if "加拿大" in country:
                dict_level_country["Canada"] += 1

            if "澳大利亚" in country:
                dict_level_country["Australia"] += 1
            if "俄罗斯" in country:
                dict_level_country["Russia"] += 1
            if "伊朗" in country:
                dict_level_country["Iran"] += 1
            if "爱尔兰" in country:
                dict_level_country["Ireland"] += 1

            if "瑞典" in country:
                dict_level_country["Sweden"] += 1
            if "巴西" in country:
                dict_level_country["Brazil"] += 1
            if "丹麦" in country:
                dict_level_country["Denmark"] += 1
            if "波兰" in country:
                dict_level_country["Poland"] += 1

            if "捷克" in country:
                dict_level_country["Czech Republic"] += 1
            if "阿根廷" in country:
                dict_level_country["Argentina"] += 1
            if "比利时" in country:
                dict_level_country["Belgium"] += 1
            if "墨西哥" in country:
                dict_level_country["Mexico"] += 1

            if "新西兰" in country:
                dict_level_country["New Zealand"] += 1
            if "荷兰" in country:
                dict_level_country["Netherlands"] += 1
            if "奥地利" in country:
                dict_level_country["Austria"] += 1
            if "土耳其" in country:
                dict_level_country["Turkey"] += 1

            if "匈牙利" in country:
                dict_level_country["Hungary"] += 1
            if "以色列" in country:
                dict_level_country["Israel"] += 1

        print(dict_level_country)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    year_2016_coutry()
