#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 10:23
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import happybase
#参考 https://blog.csdn.net/mouday/article/details/86084206

# 连接数据库
connection = happybase.Connection(host='node2', port=9090)

# 查询所有表
table_name_list = connection.tables()
print(table_name_list)
'''
# 建表
families = {
	'user_info': dict(),
	'history': dict()
}

connection.create_table('table_name', families)

# 删除表
# connection.delete_table(name, disable=False)

'''

table = connection.table('table_name')

# 获取列族信息
# info_dict = table.families()

# 添加数据
data = {
	'user_info:id': '114514',
	'history:count': '65'
}

table.put(b'xiaoming', data)

# 查询数据
row = table.row(b'xiaoming')
print(row)
# 删除数据
row = table.delete(b'xiaoming')
