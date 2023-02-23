# -*- coding: UTF-8 -*-
from MyDB import MyDB
import numpy as np
from datetime import *


def str2time(time_str):
    return datetime.strptime(time_str)


def time2str(time, format = "%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(time, format)

class Config:
    time_format = "%Y-%m-%d %H:%M:%S"
    # start_time = datetime(2022, 12, 30, 15, 3, 48)  # '2022-12-24 15:20:41'
    start_time = datetime.now()  # '2022-12-24 15:20:41'

    type2num = {
        "一": 0,
        "二": 1,
        "三": 2,
        "四": 3,
        "五": 4,
        "六": 5,

    }
    name2dict = {
        "CX": {},
        "CP": {},
        "SFZRKMC": {},
        "SFZCKMC": {},
        "BZ": {},
        "D_bottom": np.zeros((6, 24, 3), dtype = int)
    }

    time2dict = {
        "CX": start_time,
        "CP": start_time,
        "SFZRKMC": start_time,
        "SFZCKMC": start_time,
        "BZ": start_time,
        "D_bottom": start_time
    }

    total2dict = {
        "CX": 0,
        "CP": 0,
        "SFZRKMC": 0,
        "SFZCKMC": 0,
        "BZ": 0,
        "D_bottom": "D_button no num"
    }

    interval_minute = 10
    interval_second = 1


class solution:
    @staticmethod
    def count(tablename, tag, factor_str = ''):
        # 正式环境下使用
        starttime = Config.time2dict[tag]
        endtime = datetime.now()
        endtime = endtime - timedelta(seconds = 1)
        if endtime < starttime:
            starttime = endtime
        Config.time2dict[tag] = endtime + timedelta(seconds = 1)

        # 测试环境下使用
        # starttime = Config.time2dict[tag]
        # endtime = starttime + timedelta(seconds = Config.interval_second - 1)
        # nowtime = datetime.now()
        # if endtime > nowtime:
        #     endtime = nowtime
        # if endtime < starttime:
        #     starttime = endtime
        # Config.time2dict[tag] = endtime + timedelta(seconds = 1)

        # 时间转字符串
        starttime_str = "'" + time2str(starttime) + "'"
        endtime_str = "'" + time2str(endtime) + "'"

        db = MyDB()
        if tag == "CP":
            res = db.select_count_part_of_key(tablename, tag, starttime_str, endtime_str, factor_str)
        elif tag == "D_bottom":
            res = db.select_count_part_of_key(tablename, "CX", starttime_str, endtime_str, factor_str)
        else:
            res = db.select_count(tablename, tag, starttime_str, endtime_str, factor_str)

        tag_dict = Config.name2dict[tag]

        if tag == "D_bottom":
            type2num = Config.type2num
            h = starttime.hour
            for k, v in res:
                car_type = type2num[k]
                tag_dict[car_type][h][0] = car_type
                tag_dict[car_type][h][1] = h
                tag_dict[car_type][h][2] += v

        else:
            for k, v in res:
                Config.total2dict[tag] += v
                if k not in tag_dict:
                    tag_dict[k] = v
                else:
                    tag_dict[k] += v

        print("total:", Config.total2dict[tag])
        return tag_dict

    @staticmethod
    def select_interactive(tablename, condition = None, field = "*"):
        db = MyDB()
        factor_str = db.get_factor_str(condition)
        res = db.select_interactive(tablename, factor_str, field = field)
        return res


if __name__ == '__main__':

    # 交互式查询
    # 查询条件字典
    cond = {
        "SFZRKMC": "广东龙景站",
        "SFZCKMC": "广东水朗D站",
        "CX": "一型车(客)",
        "CP": "粤S88***",
        "BZ": "深圳入",
        "RKSJ": ['2020-12-21 23:30', '2020-12-21 23:40'],
        "CKSJ": ['2020-12-21 23:30', '2020-12-22 1:00'],
    }
    # 查询字段列表
    field = ",".join(['XH', 'CP', 'CX', 'SFZRKMC', 'RKSJ', 'SFZCKMC', 'CKSJ', 'BZ'])
    res = solution.select_interactive(cond, field)
    for each in res:
        print(each)

    # 统计数量，注意统计出口数量需要加上"SFZCKMC != '未知'"
    table_name = 'etc'
    for i in range(5):
        solution.count(table_name, "CX")
        solution.count(table_name, "BZ")
        solution.count(table_name, "CP")
        solution.count(table_name, 'SFZRKMC')
        solution.count(table_name, "SFZCKMC", factor_str = "SFZCKMC != 'NULL'")
