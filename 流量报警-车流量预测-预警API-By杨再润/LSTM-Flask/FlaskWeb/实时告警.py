# encoding = utf-8
import redis
import json
import flask
import datetime
from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app, resources=r'/*')	# 注册CORS, "/*" 允许访问所有api
# r = redis.Redis(host='node4', port=6379, db=0, password='redis_password',\
#                 decode_responses=True, charset='UTF-8', encoding='UTF-8')
# r.hset("my-hash-key","1","23")
def get_alarm_fromRedis():
    r = redis.Redis(host='node4', port=6379, db=0, password='redis_password', decode_responses=True, charset='UTF-8', encoding='UTF-8')
    alarm = r.hgetall("my-hash-key")
    # r.expire("my-hash-key", 20)
    if len(alarm) > 0:
        # alarm = json.loads(alarm)
        print(alarm)
        return alarm
    else:
        return None

@app.route('/alarm', methods=['GET'])
def get_alarm():
    try:
        alarm = get_alarm_fromRedis()
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
    alarm = get_alarm_fromRedis()
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

    # alarm = get_alarm_fromRedis()
    # #将alarm转换为json格式,中文显示正常
    # alarm = json.dumps(alarm, ensure_ascii=False)
    # #将alarm转换为http响应格式
    # alarm = "HTTP/1.1 200 OK\rContent-Type: application/json\r" + alarm

app.run(host="0.0.0.0", port=5000,debug=True)

