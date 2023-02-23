#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 20:12
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/

import json
import flask
import datetime
from flask_cors import CORS
from util.source_redis import get_alarm_from_redis
from util.loc import get_alarm_from_loc

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
