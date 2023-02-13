# import yagmail
import subprocess
import pymysql
import socket

ip_sql = "select * from device"
# ip_add_sql="INSERT INTO `books` VALUES ('3', '代码的力量', '明月复苏', '2', '3', '234as', '1', '<p>神不知鬼不觉的拔掉你的头发<br></p>');"
local_host_ip = socket.gethostbyname(socket.gethostname())
print(local_host_ip)


# print(type(res))

def db_connect():
    con = pymysql.connect(host='192.168.1.121',
                          user='root',
                          password='123456',
                          database='library',
                          charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = con.cursor()
    return cursor


def check_process(Process):

    cmd = 'ps axu | grep %s | grep -v grep | wc -l' % Process
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.stdout.read().decode('utf-8').strip() == '0':
        # print("sample is stop-----------")
        run_flag=0

    if res.stdout.read().decode('utf-8').strip() != '0':
        run_flag=1
        # print("sample is run-----------")

    return run_flag



if __name__ == '__main__':
    cur = db_connect()
    cur.execute(ip_sql)
    result = cur.fetchall()
    # table_cnt=cur.rowcount
    # print(cur.rowcount)
    # cur.scroll(table_cnt-1, mode='relative')  # 移动游标位置(相对位置移动，以当前位置作为起点)
    # data5 = cur.fetchall()  # 获取最后一行数据
    # print(data5)

    # row = cur.fetchone()
    # print(row)
    # print(type(result))
    # i = 0
    # for one in result:
    #     # print(i)
    #     print(result[i][0])
    #     i += 1
    #     count = i
    # # print(result[0])
    # if local_host_ip in result:
    #     while(1):
    #         flag = check_process('sample')
    #         print(flag)
    if local_host_ip in result:
        print("IP is ON table")
        flag = check_process('sample')
        print(flag)
        update_status_sql = f"update device_status set occupy_status={flag} where device_ip= {local_host_ip}"
        cur.execute(update_status_sql)

    else:
        # print(count)
        # ip_add_sql = "INSERT INTO 'device' VALUES
        print("IP is not ON table")



