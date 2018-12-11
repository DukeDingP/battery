from flask import Flask
from threading import Thread
from multiprocessing import Process
from flask import render_template
app = Flask(__name__)
import pymysql
import traceback
import 一节锂离子电池满冲满放电压
import 一节锂离子电池满冲满放电流
import time


a,b=一节锂离子电池满冲满放电压.getcycle_voltagedata() #得到电池的电压 时间信息
c,d=一节锂离子电池满冲满放电流.getcycle_currentdata()
#a,c为时间,b为电压，d为电流





db=pymysql.connect("localhost","root","123456","battery")
cursor=db.cursor()


#线程一  不断地往数据库写数据
def write2database():
    for i in range(len(b)):

        sql="INSERT INTO data (id,voltage,current,time) VALUES ('%d','%f','%f','%f');"
        try:
            cursor.execute(sql%(i+1,b[i],d[i],a[i]))
            db.commit()


        except:
            # 抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚
            print("register fall")
            cursor.close()
            # 关闭数据库连接
            db.close()


#线程二 不断地从数据库读数据
def read4database():
        for i in range(len(b)):

            time.sleep(0.01)
            sql="SELECT voltage,current,time FROM data WHERE id=('%d');"
            try:
                cursor.execute(sql%(i+1))
                db.commit()
                results = cursor.fetchone()
                print(i+1,results)

            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚

                print("register fall")
                cursor.close()
                # 关闭数据库连接
                db.close()

#线程三 测试
def test():
    i=1
    while(1):
        sql = "SELECT id FROM data;"
        #time.sleep(0.01)
       # sql="SELECT voltage,current,time FROM data WHERE id=('%d');"
        try:
            cursor.execute(sql)
            db.commit()
            try:
                results = cursor.fetchall()[-1][0]

                print(results,i)
                if results==i:
                    # time.sleep(0.01)
                    sql = "SELECT voltage,current,time FROM data WHERE id=('%d');"
                    try:
                        cursor.execute(sql % (i))
                        db.commit()
                        results = cursor.fetchone()
                        print(i , results)
                        i+=1

                    except:
                        # 抛出错误信息
                        traceback.print_exc()
                        # 如果发生错误则回滚

                        print("register fall")
                        cursor.close()
                        # 关闭数据库连接
                        db.close()
            except:
                print("waiting for data")


        except:
            # 抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚

            print("register fall")
            cursor.close()
            # 关闭数据库连接
            db.close()

#线程四 使用trigger
def trigger():
    i=None
    while (1):
        sql = "SELECT num FROM `condition` where id=1;"
        # time.sleep(0.01)
        # sql="SELECT voltage,current,time FROM data WHERE id=('%d');"
        try:
            cursor.execute(sql)
            db.commit()
            trigger=cursor.fetchone()[0]
            if trigger!=i:
                sql = "SELECT voltage,current,time from data order by id desc LIMIT 1"
                try:
                    cursor.execute(sql)
                    db.commit()
                    results = cursor.fetchone()
                    print(i+1,results)


                except:
                    # 抛出错误信息
                    traceback.print_exc()
                    # 如果发生错误则回滚

                    print("register fall")
                    cursor.close()
                    # 关闭数据库连接
                    db.close()
            i=trigger

        except:
            # 抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚
            print("register fall")
            cursor.close()
            # 关闭数据库连接
            db.close()

if __name__ == '__main__':
    #part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
    t1=Process(target=write2database)

    t1.start()

    # t2 = Process(target=read4database)
    #     # time.sleep(1)
    #     # t2.start()

    # t3=Process(target=test)
    #
    # t3.start()

#使用trigger
    t4=Process(target=trigger)
    t4.start()



# 默认路径访问登录页面
# @app.route('/')
# def login():
#     return render_template('梯次电池等级评估.html')
#
# if __name__ == '__main__':
#
#     app.run(debug=True)


#单纯 mysql数据库 读比写快
#设计到逻辑判断 写比读快
#线程二设计思路 延迟读数据 留有足够长的时间来保证数据库完成写入   没有鲁棒性，牺牲效率
#线程三 设计思路 判断最后一数据更新 读取新数据   逻辑判断耗费时间 遇到太快造成数据丢失
#线程四 目标：每次写入数据库即可发现并更新 兼具鲁棒性与效率 触发器 完美