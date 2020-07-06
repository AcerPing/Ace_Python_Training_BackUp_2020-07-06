import pymysql
import os
import prettytable

#起始畫面－輸入密碼及Port
PASS=input("請輸入資料庫密碼：")
PT=input("請輸入資料庫的Port：")

localhost = "localhost"

#Port設定方法一:當有輸入資料庫的Port時，則改設定localhost
if PT != None: #當Port有輸入代碼時
    localhost = "localhost" + ":" + PT #則localhost會是"localhost:代碼"(純文字)

os.system("cls") #清除剛輸入密碼及Port的畫面

def table(): #定義函數
    form=prettytable.PrettyTable(["編號","姓名","生日","地址"],encoding="utf8") #建立一個PrettyTable表格
    c.execute("SELECT * FROM `member`")
    for d in c.fetchall():
        # print(d)
        form.add_row([d[0],d[1],d[2],d[3]])
    print()
    print(form)
    print()

x = None #起始值x為None

while x!="0": #當x不等於0時，顯示Menu

    #連結 MySQL
    e=pymysql.connect(host="localhost",user="root",passwd=PASS ,
                    db="python_ai",charset="utf8",port=PT) 
    
    c=e.cursor() #取得指令操作變數

    #當x不等於0時，顯示Menu
    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")

    #輸入x資料
    x=input("操作:")

    #TODO:當輸入者按下"0"時，則離開程式
    if x == "0":
        os.system("cls")
        e.close()
        break

    #TODO:當輸入者按下"1"時，則顯示會員列表
    if x == "1":
        table() #呼叫表格函式
        e.close()
        
    #TODO:當輸入者按下"2"時，則新增會員資料
    if x == "2":
        print("\n")
        c.execute(
        "INSERT INTO `member`(`name`,`birthday`,`address`)"+
        " VALUES(%s,%s,%s)"
        , [
        input("請輸入會員姓名:"),
        input("請輸入會員生日:"),
        input("請輸入會員地址：")])
        print("\n")
        e.commit()
        os.system("cls")
        e.close()
 
    
    #TODO:當輸入者按下"3"時，則修改會員資料
    if x == "3":
        table()
        #TODO:修改該會員資料
        print("\n")
        number=int(input("請輸入代碼:"))
        name = input("請輸入會員姓名:"),
        birthday = input("請輸入會員生日:"),
        address = input("請輸入會員地址：")
        c.execute("UPDATE `member` SET `name` = %s, `birthday` = %s, `address` = %s WHERE `id` = %s", [name,birthday,address,number])
        print("\n")
        e.commit()
        e.close()
        
    #TODO:當輸入者按下"4"時，則刪除該筆會員資料
    if x == "4":
        table()
        print("\n")
        c.execute(
        "DELETE FROM `member` WHERE `id`=%s",
        [input("請輸入id編號:")])
        print("\n")
        e.commit()
        e.close()