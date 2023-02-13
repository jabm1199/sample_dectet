import pymysql


def db_connect():
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='123456',
                          database='library',
                          charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = con.cursor()
    return cursor


if __name__ == '__main__':
    sql = "select * from device"

try:
    cur = db_connect()
    cur.execute(sql)
    result = cur.fetchall()
    for data in result:
        print(data)
except Exception:
    print("查询失败")
