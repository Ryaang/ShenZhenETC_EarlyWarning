#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 20:09
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import happybase


#建立happybase连接，中文显示正常
# connection = happybase.Connection(host='node2', port=9090, protocol='compact', \
#                                   transport='buffered', timeout=10000, autoconnect=True, table_prefix=None, \
#                                   table_prefix_separator=b':', compat='0.98')
# connection.open()
# connection = happybase.Connection(host='node2', port=9090)
#查看所有表
#建立happybase连接，去除b'前缀
connection = happybase.Connection(host='node2', port=9090)
tables = connection.tables()
print(tables)
#查看表'ETC'的所有数据，toStr=True表示将数据转换为字符串

table = connection.table('static')
for key, data in table.scan():
    print(key.decode('utf-8'), data)
#在表’test’中插入一条数据,数据格式为：b'i这个度': {b'info:col1': b'value1'}，中文编码为ascii

# table.put('i这个度'.encode(), {b'info:col1': b'value1'})

bat = table.batch()

#将data/data1.txt中的数据插入到表'test'中
with open('../data/data1.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if line[0] == 'D':
            continue
        key, value1,value2,value3 =  line.split(',')
        bat.put(key, {b'LTZX:minute': value1,b'SLD:minute': value2,b'SSHN:minute': value3})
bat.send()

#在创建表'static',列族有'LTZX','SLD','SSHN'
# connection.create_table('static', {'LTZX': dict(), 'SLD': dict(), 'SSHN': dict()})

