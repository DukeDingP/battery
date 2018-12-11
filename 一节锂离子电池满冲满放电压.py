import xlrd
import matplotlib.pyplot as plt
import 中文
xlsfile = r"满充满放实验.xlsx"    # 打开指定路径中的xls文件
book = xlrd.open_workbook(xlsfile)#得到Excel文件的book对象，实例化对象
sheet0 = book.sheet_by_index(0) # 通过sheet索引获得sheet对象
sheet0.row_values(0)
sheet0.row_values(1)
sheet0.row_values(2)
#plt.plot(sheet0.row_values(2),sheet0.row_values(0))

font1={"size":15}
def removenull(a):
    for i in range(len(a)):
        if a[i]=="":
            a=a[:i]
            break
    return a


def getcycle_voltagedata():
    x,y=sheet0.row_values(2),sheet0.row_values(1)
    x=[i/3600 for i in x]
    #plt.plot(x,y,c="orange")
   # print(sheet0.row_values(6))


    x1=removenull(sheet0.row_values(6))
   # print(sheet0.row_values(2)[-1])
    x1=[i+sheet0.row_values(2)[-1] for i in x1]
    x1=[i/3600 for i in x1]
    y1=removenull(sheet0.row_values(5))
   # print(type(x))


    p,=plt.plot(x+x1,y+y1,c="orange")
    plt.grid()
    plt.legend([p],["充放电电压"],loc=3,prop=font1)
    plt.xlabel("充放电时间/h",size=15)
    plt.ylabel("充放电电压/V",size=15)
    plt.show()
    return (x+x1,y+y1)

