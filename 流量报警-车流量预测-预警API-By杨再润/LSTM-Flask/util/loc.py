#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 21:08
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import random
import datetime
'''
这个data包含一个列表
要传的就是最近的站口流量数据，我设置的是10秒更新一次
{alertdetail:’报警内容’,alertvalue:’流量告警值’,createtime:’时间’,gatewayno:’站口名称’,provinceName:’地址’}
这个地址信息可以直接给个广东省就行，也可以后期删除不需要这个数据
'''

#create_time加1秒
def add_time():
    now = datetime.datetime.now()
    now = now + datetime.timedelta(seconds=1)
    return now.strftime('%Y-%m-%d %H:%M:%S')

def get_alarm_from_loc():
    data = [
        {
            "alertdetail": "流量告警",
            "alertvalue": random.randint(10, 30),
            "createtime": add_time(),
            "gatewayno": "松山湖南",
            "provinceName": "深圳市"
        },
        {
            "alertdetail": "流量告警",
            "alertvalue": random.randint(10, 30),
            "createtime": add_time(),
            "gatewayno": "广东罗田主线站",
            "provinceName": "深圳市"
        },
        {
            "alertdetail": "流量告警",
            "alertvalue": random.randint(10, 30),
            "createtime": add_time(),
            "gatewayno": "广东水朗D站",
            "provinceName": "深圳市"
        }
    ]

    #如果alertvalue小于20，则alertdetail为正常，否则为流量告警
    for i in data:
        if i['alertvalue'] < 20:
            i['alertdetail'] = '正常'
        else:
            i['alertdetail'] = '流量告警'
    return data

if __name__ == '__main__':
    print(get_alarm_from_loc())


