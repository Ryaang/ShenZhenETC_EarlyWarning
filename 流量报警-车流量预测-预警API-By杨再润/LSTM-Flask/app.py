#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 20:12
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/

import json
import flask
import datetime

import numpy as np
from flask import request
from flask_cors import CORS
from util.source_redis import get_alarm_from_redis
from util.loc import get_alarm_from_loc
from util.hloc import getHbaseCount_minute_loc
from inference import inference

app = flask.Flask(__name__)
CORS(app, resources=r'/*')	# 注册CORS, "/*" 允许访问所有api


@app.route('/alarm', methods=['GET'])
def get_alarm():
    try:
        alarm = get_alarm_from_redis()
        # alarm加入时间戳
        alarm['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ret = {
            "status":0,
            "msg": "",
            "data": alarm
        }


        return json.dumps(ret, ensure_ascii=False)
            # return flask.jsonify(alarm)
    except Exception as e:
        return flask.jsonify({"status":0, "msg": "暂无告警信息！", "data": None})

@app.route('/alarm-empty', methods=['GET'])
def empty_alarm():
    l=[]
    l.append({"status":0, "msg": "暂无告警信息！", "data": None})
    return flask.jsonify(l)


@app.route('/alarm-grc', methods=['GET'])
def grc_alarm():
    alarm = get_alarm_from_redis()
    # alarm加入时间戳
    alarm['时间'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ret = {
        "status":0,
        "msg": "",
        "data": str(alarm)[1:-1]
    }
    if alarm:
        return json.dumps(ret, ensure_ascii=False)
        # return flask.jsonify(alarm)
    else:
        return flask.jsonify({"status":0, "msg": "暂无告警信息！", "data": None})

@app.route('/right-bottom', methods=['GET'])
def right_bottom():
    return json.dumps(get_alarm_from_loc())

@app.route('/i',methods=['GET'])#临时测试用
def predict():
    x = [
        [5, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [7, 8, 9],
        [0.7, 1, 2],
        [10, 2, 3],
        [6, 6, 6]
    ]
    ans = inference(x)
    print(ans)
    return str(ans)

@app.route('/predict',methods=['GET'])
def predict_minute():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    x_ori = getHbaseCount_minute_loc(time = now)
    predict_value = inference(x_ori)
    single_value = str(predict_value[0])
    return json.dumps(single_value)

#返回如 dateList:['2021-11', '2021-12', '2022-01', '2022-02', '2022-03'] 以及对应的numList:[]
@app.route('/right-top',methods=['GET'])
def right_top():
    #最近十分钟以H:MM的格式存储到列表里
    dateList = []
    numList = []
    numList2 = []
    numList3 = []
    for i in range(9):
        dateList.append((datetime.datetime.now() - datetime.timedelta(minutes=i)).strftime('%H:%M'))
    dateList.reverse()
    allNumList = getHbaseCount_minute_loc(time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #取allNumList中每个元素的第一个值，即每个元素的第一个值为该分钟的总数
    for i in range(len(allNumList)):
        numList.append(allNumList[i][0]+6)
        numList2.append(allNumList[i][1]+6)
        numList3.append(allNumList[i][2]+6)
    return json.dumps({"dateList":dateList,"numList":numList,"numList2":numList2,"numList3":numList3})

@app.route('/origin',methods=['GET'])
def origin():
    dateList = []
    numList = []
    numList2 = []
    numList3 = []
    res = {
      "status": 0,
      "msg": "",
      "data": {
        "categories": [#x轴
        ],
        "series": [
          {
            "name": "罗田主线站",
            "data": [
            ]
          },
          {
            "name": "水朗D站",
            "data": []
          },
          {
            "name": "松山湖南站",
            "data": [
            ]
          }
        ]
      }
    }
    try:
        #用flask解析前端传来的参数中的conditions列表
        conditions = request.args.get('conditions')
        conditions = json.loads(conditions)
    except:
        return json.dumps(res)
    st ,ed ,rg = conditions[0]['v'] , conditions[1]['v'] , conditions[2]['v']
    st = '2020-12-22 '+st+':00'
    ed = '2020-12-22 '+ed+':00'
    allNumList = getHbaseCount_minute_loc(time=st)
    #将st和ed转换为时间
    st = datetime.datetime.strptime(st, '%Y-%m-%d %H:%M:%S')
    ed = datetime.datetime.strptime(ed, '%Y-%m-%d %H:%M:%S')
    #将从st到ed的每个分钟存入dateList，如果已经存了9个时间点，就不再存
    while st <= ed and len(dateList) < 9:
        dateList.append(st.strftime('%H:%M'))
        st += datetime.timedelta(minutes=1)
    #取allNumList中每个元素的第一个值，即每个元素的第一个值为该分钟的总数
    for i in range(len(allNumList)):
        numList.append(allNumList[i][0])
        numList2.append(allNumList[i][1])
        numList3.append(allNumList[i][2])

    res['data']['categories'] = dateList
    res['data']['series'][0]['data'] = numList
    res['data']['series'][1]['data'] = numList2
    res['data']['series'][2]['data'] = numList3
    return json.dumps(res)

@app.route('/bgpredict',methods=['GET'])
def bgpredict():
    #用flask解析前端传来的参数中的conditions列表
    conditions = request.args.get('conditions')
    conditions = json.loads(conditions)
    st ,ed ,rg = conditions[0]['v'] , conditions[1]['v'] , conditions[2]['v']
    st = '2020-12-22 '+st+':00'
    ed = '2020-12-22 '+ed+':00'
    x_ori = getHbaseCount_minute_loc(time=st)
    predict_value1 = inference(x_ori)
    predict_value1 = str(predict_value1[0])
    #将x_ori第一列和第二列交换
    x_ori = np.array(x_ori)
    x_ori[:,[0,1]] = x_ori[:,[1,0]]
    #将交换的x_ori存为新的列表
    x_ori_2 = x_ori.tolist()
    predict_value2 = inference(x_ori_2)
    predict_value2 = str(predict_value2[0])
    #将x_ori第一列和第三列交换
    x_ori[:,[0,2]] = x_ori[:,[2,0]]
    #将交换的x_ori存为新的列表
    x_ori_3 = x_ori.tolist()
    predict_value3 = inference(x_ori_3)
    predict_value3 = str(predict_value3[0])
    #把ed加一分钟装入列表
    dateList = []
    numList = []
    numList2 = []
    numList3 = []
    dateList.append('前一分钟')
    dateList.append('预计下一分钟')
    numList2.append(str(x_ori_3[8][2]))
    numList.append(str(x_ori[8][1]))
    numList3.append(str(x_ori[8][0]))
    numList.append(predict_value1)
    numList2.append(predict_value2)
    numList3.append(predict_value3)
    res = {
      "status": 0,
      "msg": "",
      "data": {
        "categories": [#x轴
        ],
        "series": [
          {
            "name": "罗田主线站",
            "data": [
            ]
          },
          {
            "name": "水朗D站",
            "data": []
          },
          {
            "name": "松山湖南站",
            "data": [
            ]
          }
        ]
      }
    }
    res['data']['categories'] = dateList
    res['data']['series'][0]['data'] = numList
    res['data']['series'][1]['data'] = numList2
    res['data']['series'][2]['data'] = numList3
    return json.dumps(res)


@app.errorhandler(400)
def crack_response(e):
    hurl = flask.request.remote_addr     #请求来源的ip地址
    hmsg =                     "Congratulates %s !\
                                    You are an Administrator now,\
                                    But you got the wrong token,\
                                    the right token is 'FUCK YOU HACKER!' " % hurl
    print("异常请求ip"+str(hurl))
    return hmsg

app.run(host="0.0.0.0", port=5000,debug=True)
