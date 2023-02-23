import pymysql


class DbConfig:
    # 本地
    # user = 'root'
    # password = "123456"
    # host = '127.0.0.1'
    # database = 'test'
    # port = 3306

    # 服务器MyCat
    user = 'root'
    password = "123456"
    host = '124.71.207.74'
    database = 'MYETCDB'
    port = 8066

    # 服务器MySQL
    # user = 'root'
    # password = "123456"
    # host = '124.71.207.74'
    # database = 'myetc'
    # port = 3306


class MyDB:
    def __init__(self):
        self.conn = pymysql.connect(
            user = DbConfig.user,
            password = DbConfig.password,
            host = DbConfig.host,
            database = DbConfig.database,
            port = DbConfig.port
        )
        self.cursor = self.conn.cursor()
        self.field = ('XH', 'CP', 'CX', 'SFZRKMC', 'RKSJ', 'SFZCKMC', 'CKSJ', 'BZ')

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_factor_str(self, condition: dict):
        """获得查询条件"""
        factor_str = ""
        if condition is None:
            return factor_str
        for k, v in condition.items():
            if k == "CKSJ" or k == "RKSJ":
                factor_str += k + " between " + "'" + v[0] + "'" + " and " + "'" + v[1] + "'" + " and "
            elif k == "startXH":
                factor_str += "XH" + " > " + str(v) + " and "
            else:
                factor_str += k + " = " + "'" + v + "'" + " and "
        factor_str = factor_str[:-5]
        return factor_str

    def select_interactive(self, table_name, factor_str = "", field = "*"):
        """
        交互式查询
        :param table_name: 表名
        :param factor_str: 查询条件
        :param field: 查询字段,字符串形式,中间使用逗号隔开
        :return:
        """
        if factor_str == "":
            sql = f"select {field} from {table_name} order by XH"
        else:
            sql = f"select {field} from {table_name} where {factor_str} order by XH"
        try:
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            print("查询结果数量为：", len(res))
            return res
        except Exception as e:
            print("查询失败\n", e)

    def select_count(self, table_name, field, starttime, endtime, factor_str = ''):
        """
        增量查询各字段数量
        :param table_name: 表名
        :param field: 所要查询的字段
        :param starttime: 开始时间
        :param endtime: 结束时间
        :param factor_str: 查询条件
        :return:
        """
        if factor_str == '':
            sql = f"select {field},count({field}) from {table_name} where CKSJ between {starttime} and {endtime} group by {field}"
        else:
            sql = f"select {field},count({field}) from {table_name} where {factor_str} and CKSJ between {starttime} and {endtime} group by {field}"
        try:
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            # print("查询结果为：", res)
            print("查询结果数量为：", len(res))
            return res
        except Exception as e:
            print("查询失败\n", e)

    def select_count_part_of_key(self, table_name, field, starttime, endtime, factor_str = ''):
        """
        增量查询部分字段
        :param table_name:表名
        :param field:查询字段
        :param starttime:开始时间
        :param endtime:结束时间
        :param factor_str:查询条件
        :return:
        """
        # 样例SQL
        # select left(CP,1),count(CP) from etc where RKSJ between '2020-12-21 23:20' and '2020-12-22 00:00' group by left(CP,1);
        if factor_str == '':
            sql = f"select left({field},1),count({field}) from {table_name} where RKSJ between {starttime} and {endtime} group by left({field},1) "
        else:
            sql = f"select left({field},1),count({field}) from {table_name} where {factor_str} and RKSJ between {starttime} and {endtime} group by left({field},1)"
        try:
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print("查询失败\n", e)

        def select_count_all(self, table_name, field, factor_str = ''):
            """全量查询"""
            if factor_str == '':
                sql = f"select {field},count({field}) from {table_name} group by {field}"
            else:
                sql = f"select {field},count({field}) from {table_name} where {factor_str} group by {field}"
            try:
                print(sql)
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                return res
            except Exception as e:
                print("查询失败\n", e)


if __name__ == '__main__':
    db = MyDB()
    table_name = 'etc'
    cond = {
        "SFZRKMC": "广东龙景站",
        "SFZCKMC": "广东水朗D站",
        "CX": "一型车(客)",
        "CP": "粤S88***",
        "BZ": "深圳入",
        "RKSJ": ['2020-12-21 23:30', '2020-12-21 23:40'],
        "CKSJ": ['2020-12-21 23:30', '2020-12-22 1:00'],
    }

    factor = db.get_factor_str(cond)
    print(factor)
    res = db.select_interactive(table_name, factor_str = factor)
    for each in res:
        print(each)
