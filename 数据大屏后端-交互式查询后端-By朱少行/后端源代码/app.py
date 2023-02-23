# -*- coding: UTF-8 -*-
import os
from flask import Flask, request, render_template, send_file, send_from_directory
from flask_cors import CORS
from solution import *
import csv
import json
import pandas as pd

app = Flask(__name__)
app.debug = True
CORS(app, resources = r'/*')  # 注册CORS, "/*" 允许访问所有api

key = ['XH', 'CP', 'CX', 'SFZRKMC', 'RKSJ', 'CKSJ', 'SFZCKMC', 'BZ']


@app.errorhandler(400)
def crack_response(e):
    hurl = "36.150.60.24"  # 请求来源的ip地址
    hmsg = "Congratulates %s !\
                                    You are an Administrator now,\
                                    But you got the wrong token,\
                                    the right token is 'FUCK YOU HACKER!' " % hurl
    print("异常请求ip" + str(hurl))
    return hmsg


def load_CP_dict_from_sql():
    CP_dict = {}
    db = MyDB()
    sql = "select * from cp_map"
    db.cursor.execute(sql)
    res = db.cursor.fetchall()
    for k, v in res:
        CP_dict[k] = v
    return CP_dict


def load_CP_dict_from_file(path):
    CP_dict = {}
    with open(path, encoding = 'gbk') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            v, k = line
            CP_dict[k] = v
    return CP_dict


@app.route("/left_top")
def solve_left_top():
    # {totalNum:'车辆总数',onlineNum:'三型车以下',offlineNum:'四型车以上'}
    data = {
        "onlineNum": 0,
        "offlineNum": 0,
        "totalNum": 0
    }

    res = solution.count(tablename, 'CX')
    for k, v in res.items():
        data["totalNum"] += v
        if k[0] <= '三':
            data["onlineNum"] += v
        else:
            data["offlineNum"] += v
    print("left_top\n", data)
    return json.dumps(data)


@app.route("/left_center")
def solve_left_center():
    map2name = {
        '广东罗田主线站': 'lockNum',
        '广东水朗D站': 'onlineNum',
        '松山湖南': 'offlineNum'
    }
    data = {
        "lockNum": 0,
        "onlineNum": 0,
        "offlineNum": 0,
        "totalNum": 0
    }
    res = solution.count(tablename, 'SFZCKMC', factor_str = "SFZCKMC != 'NULL'")
    for k, v in res.items():
        key = map2name[k]
        data[key] += v
        data["totalNum"] += v
    print("left_center\n", data)
    return json.dumps(data)


@app.route("/center_map", methods = ['POST', 'GET'])
def solve_center_map():
    data = []
    res = solution.count(tablename, 'CP')

    for k, v in res.items():
        d = {}
        key = CP_dict[k]
        d['name'] = key
        d['value'] = v
        data.append(d)
    print("center_map\n", data)
    return json.dumps(data, ensure_ascii = False)


@app.route("/center_bottom")
def solve_center_bottom():
    # barData给的是客车数据
    # lineData给的是货车数据
    # rateData给的是客车数据除以货车数据后的比率乘以100
    data = {
        "barData": [0, 0, 0, 0],
        "lineData": [0, 0, 0, 0],
        "rateData": [0, 0, 0, 0]
    }

    map2name = {'客': "barData", '货': "lineData"}
    map2idx = {'一': 0, '二': 1, '三': 2, '四': 3}

    res = solution.count(tablename, 'CX')
    for k, v in res.items():

        if k[0] not in map2idx:
            continue
        name = k[-2]
        idx = k[0]
        data[map2name[name]][map2idx[idx]] = v
    barData = data["barData"]
    lineData = data["lineData"]
    rateData = data["rateData"]
    for idx, v in enumerate(lineData):
        if v == 0:
            continue
        rateData[idx] = round(barData[idx] / lineData[idx] * 100)
    print("center_bottom\n", data)
    return json.dumps(data)


@app.route("/right_center")
def solve_right_center():
    data = []
    res = solution.count(tablename, 'CX')
    for k, v in res.items():
        d = {"name": k, "value": v}
        data.append(d)
    print("right_center\n", data)
    return json.dumps(data, ensure_ascii = False)


@app.route("/interactive", methods = ['POST', 'GET'])
def solve_interactive():
    global last_select_dict
    try:
        d = request.get_data(as_text = True)
        select_dict = json.loads(d)
        last_select_dict = select_dict
    except Exception as e:
        return "查询条件格式错误！&nbsp;&nbsp;错误信息为：<br><p style= 'color:red'>{}</p>".format(e)

    try:
        cond = select_dict['cond']
    except Exception as e:
        return "字典格式错误！缺少'cond'字段&nbsp;&nbsp;错误信息为：<br><p style= 'color:red'>{}</p>".format(e)

    if 'field_list' in select_dict:
        field_list = select_dict['field_list']
        field = ",".join(field_list)
    else:
        field = '*'

    # 测试条件
    # field = '*'
    # cond = {
    #     "SFZRKMC": "广东龙景站",
    #     "SFZCKMC": "广东水朗D站",
    #     "CX": "一型车(客)",
    #     "CP": "粤S88***",
    #     "BZ": "深圳入",
    #     "RKSJ": ['2020-12-21 23:30', '2020-12-21 23:40'],
    #     "CKSJ": ['2020-12-21 23:30', '2020-12-22 1:00'],
    # }

    data = solution.select_interactive(tablename, cond, field = field)
    print("solve_interactive\n", data)
    return json.dumps(data, ensure_ascii = False)


@app.route("/download", methods = ['POST', 'GET'])
def solve_download():
    # try:
    #     d = request.get_data(as_text = True)
    #     print(d)
    #     select_dict = json.loads(d)
    # except Exception as e:
    #     return "查询条件格式错误！&nbsp;&nbsp;错误信息为：<br><p style= 'color:red'>{}</p>".format(e)

    select_dict = last_select_dict
    try:
        cond = select_dict['cond']
    except Exception as e:
        return "字典格式错误！缺少'cond'字段&nbsp;&nbsp;错误信息为：<br><p style= 'color:red'>{}</p>".format(e)

    if 'filetype' in select_dict:
        filetype = select_dict['filetype']
    else:
        filetype = "csv"

    if 'field_list' in select_dict:
        field_list = select_dict['field_list']
        field = ",".join(field_list)
    else:
        field = '*'

    if filetype == "csv":
        file_path = "./TempFile/data.csv"
    elif filetype == "xlsx":
        file_path = "./TempFile/data.xlsx"
    else:
        return "<p style= 'color:red'>字典格式错误！缺少filetype字段或者filetype类型错误</p>"

    if not os.path.exists("./TempFile"):
        os.mkdir("./TempFile")

    data = solution.select_interactive(tablename, cond, field = field)
    df = pd.DataFrame(data, columns = key)

    if filetype == "csv":
        df.to_csv(file_path, index = False)
    else:
        df.to_excel(file_path, index = False)
    print("solve_download\nfilepath={}".format(file_path))
    return send_file(file_path, as_attachment = True)


@app.route("/")
def solve():
    return render_template("API.html")


@app.route("/D_bottom")
def solve_3D_bottom():
    res = solution.count(tablename, "D_bottom")
    data = res.reshape(6 * 24, 3).tolist()
    return json.dumps(data)


if __name__ == '__main__':
    tablename = 'etc'
    cp_path = 'cp_map.csv'
    last_select_dict = {
        'cond': {
            "SFZCKMC": "广东水朗D站",
            "CX": "一型车(客)",
            "CP": "粤S88***",
            "BZ": "深圳入",
        },
        'filetype': "xlsx"
    }

    # CP_dict = load_CP_dict_from_file(cp_path)
    CP_dict = load_CP_dict_from_sql()
    app.run(host = '0.0.0.0', port = 5000, debug = True)
