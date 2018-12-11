import pymysql
import traceback
db=pymysql.connect("localhost","root","123456","battery")
cursor=db.cursor()

sql = "DELETE FROM data;"
try:
    cursor.execute(sql)
    db.commit()


except:
    # 抛出错误信息
    traceback.print_exc()
    # 如果发生错误则回滚
    print("register fall")
    cursor.close()
    # 关闭数据库连接
    db.close()
