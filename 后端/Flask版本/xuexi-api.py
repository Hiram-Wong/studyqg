# -*- encoding: utf-8 -*-

from flask import Flask, request, Response
import pymysql, json, requests

from flask_cors import *

app = Flask(__name__)


# 解决跨域问题
CORS(app, supports_credentials=True)


def mysql():
    conn = pymysql.connect(
        host='localhost',
        user='study',
        passwd='123456',
        db='study',
        charset='utf8'
    )
    return conn


def search(key):
    mysqls = mysql()
    cur = mysqls.cursor()
    sql_search = 'SELECT * FROM study WHERE question LIKE "%{}%"'.format(key)
    # sql_total = 'SELECT COUNT(*) FROM study'
    res = cur.execute(sql_search)
    data_search = cur.fetchall()
    # res = cur.execute(sql_total)
    # data_total = cur.fetchone()
    search_all_list = []
    for i in range(len(data_search)):
        search_list = {}
        search_list['id'] = data_search[i][0]
        search_list['question'] = data_search[i][1]
        search_list['answer'] = data_search[i][2]
        search_list['A'] = data_search[i][3]
        search_list['B'] = data_search[i][4]
        search_list['C'] = data_search[i][5]
        search_list['D'] = data_search[i][6]
        search_list['answer_detail'] = data_search[i][2] + ":" + search_list[data_search[i][2]]
        search_all_list.append(search_list)
    res = {
        'code': 200,
        'msg': '获取成功',
        # 'total': data_total[0],
        'data': search_all_list
    }
    print(res)
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')


def detail(id):
    mysqls = mysql()
    cur = mysqls.cursor()
    sql = 'SELECT * FROM study WHERE id = {}'.format(id)
    cur.execute(sql)
    data = cur.fetchone()
    print(data)
    arrlist = {}
    for i in data:
        arrlist['question'] = data[1]
        arrlist['answer'] = data[2]
        arrlist['A'] = data[3]
        arrlist['B'] = data[4]
        arrlist['C'] = data[5]
        arrlist['D'] = data[6]
    res = {
        'code': 200,
        'msg': 'success',
        'data': arrlist
    }
    print(res)
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')


@app.route('/search', methods=['GET'])
def index():
    key = request.args.get('kw')
    res = search(key)
    return res


@app.route('/banner', methods=['GET'])
def banner():
    res = {
        'status': '200',
        'msg': '获取成功',
        'data': [{
            'id': 0,
            'type': 'image',
            'url': 'https://ae01.alicdn.com/kf/H4d220eff215643c8a99c02fc5c790624s.png'
        }, {
            'id': 1,
            'type': 'image',
            'url': 'https://ae01.alicdn.com/kf/H9ca42dcbfd2e4631997c4d137be23450e.png'
        }, {
            'id': 2,
            'type': 'image',
            'url': 'https://ae01.alicdn.com/kf/H8243d5fcd06f4c9ebe2b52b982f65762a.png'
        }]
    }
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')


@app.route('/basic', methods=['GET'])
def base():
    mysqls = mysql()
    cur = mysqls.cursor()
    sql_total = 'SELECT COUNT(*) FROM study'
    cur.execute(sql_total)
    total = cur.fetchone()[0]
    versation_res = requests.get('http://127.0.0.1:8000/log').json()
    versation = versation_res['data'][-1]['versation']
    res = {
        'status': '200',
        'msg': '获取成功',
        'data': {
            "question_total": total,
            "versation": versation
        }
    }
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')


@app.route('/id', methods=['GET'])
def id():
    id = request.args.get('id')
    res = detail(id)
    return res


@app.route('/log', methods=['GET'])
def log():
    res = {
        'status': '200',
        'msg': '获取成功',
        'data': [{
            'versation': '1.0.0',
            'time': '2020/03/31',
            'description': '完成基础功能的开发'
        }, {
            'versation': '1.0.0',
            'time': '2020/04/01',
            'description': '微信小程序1.0.0上线'
        }, {
            'versation': '1.1.0',
            'time': '2020/04/02',
            'description': '1.完成语音识别功能\n2.完成详情页的开发\n3.加入客服解答'
        }, {
            'versation': '1.1.0',
            'time': '2020/04/03',
            'description': '完成1.1.0的审核，微信小程序端线上全量推送'
        }, {
            'versation': '1.2.0',
            'time': '2020/04/03',
            'description': '给适当的页面增加回顶部'
        }, {
            'versation': '1.2.0',
            'time': '2020/04/5',
            'description': '完成1.2.0的审核，微信小程序端线上全量推送'
        }, {
            'versation': '1.2.1',
            'time': '2020/04/11',
            'description': '1.修复部分资源失效\n2.完成QQ小程序1.2.1的兼容[去除语音识别和客服功能]'
        }, {
            'versation': '1.2.1',
            'time': '2020/04/13',
            'description': '1.完成1.2.1的审核，微信小程序端线上全量推送\n2.QQ小程序1.2.1上线'
        }]
    }
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0', '2333', debug=False)
