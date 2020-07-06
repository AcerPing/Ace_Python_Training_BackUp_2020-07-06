import pymysql
import os
import prettytable

#起始畫面
PASS=input("請輸入資料庫密碼：")

##Port設定方法二:首先嘗試輸入資料庫的Port
try:
    PT=int(input("請輸入資料庫的Port：")) #文字轉數字
# 當輸入資料庫為空白的時後，會有ValueError的現象，則將PT設為None
except ValueError: 
    PT=None

os.system("cls") #清除剛輸入密碼及Port的畫面

#TODO:若已有"會員編號"，則"姓名","生日","地址"顯示空白，只顯示電話
def table(): #定義函數
    form=prettytable.PrettyTable(["編號","姓名","生日","地址","電話"],encoding="utf8") #建立一個PrettyTable表格
    c.execute("SELECT `a`.*,`b`.`tel` FROM `member` as `a` LEFT JOIN `tel` as `b` ON `a`.`id` =  `b`.`member_id`")
    D=[]
    for d in c.fetchall():
        if d[0] not in D:
            D.append(d[0])
            form.add_row([d[0],d[1],d[2],d[3],d[4]])
        elif d[0] in D:
            form.add_row([" ","  ","  ","  ",d[4]])
    print()
    print(form)
    print()

x = None #起始值x為None

while x!="0": 

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
    print("(5) 新增會員的電話")
    print("(6) 刪除會員的電話")

    #輸入x資料
    x=input("操作:")

    #TODO:當輸入者按下"0"時，則離開程式
    if x == "0":
        os.system("cls") #清除畫面
        e.close() #關閉 MySQL 連線
        break #中斷迴圈

    #TODO:當輸入者按下"1"時，則顯示會員列表
    if x == "1":
        table() #呼叫表格函式
        e.close() #關閉 MySQL 連線
        
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
        e.close()
        os.system("cls") #每次執行完皆清除畫面 
 
    
    #TODO:當輸入者按下"3"時，則修改會員資料
    if x == "3":
        table()#呼叫表格函式

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
        os.system("cls") #每次執行完皆清除畫面 
       
    #TODO:當輸入者按下"4"時，則刪除該筆會員資料
    if x == "4":
        table()#呼叫表格函式

        print()
        c.execute(
        "DELETE FROM `member` WHERE `id`=%s",
        [input("請輸入id編號:")])
        print()

        e.commit()
        e.close()
        os.system("cls") #每次執行完皆清除畫面 

    #TODO:當輸入者按下"5"時，則新增電話
    if x == "5":
        table()#呼叫表格函式

        print()
        c.execute("INSERT INTO `tel`(`member_id`,`tel`) VALUES(%s,%s)",[input("請選擇要添加電話的會員編號："),input("請輸入電話：")])
        print()

        e.commit()
        e.close()
        os.system("cls") #每次執行完皆清除畫面 

    #TODO:當輸入者按下"6"時，則刪除電話
    if x == "6":
        table()#呼叫表格函式

        #TODO:Select→詢問要刪除哪筆電話(秀表格)→刪除
        #篩選後的`tel`表格
        phone=prettytable.PrettyTable(["編號","電話"],encoding="utf8") #建立一個PrettyTable表格
        c.execute("SELECT * FROM `tel` WHERE `member_id`=%s",[input("請選擇要刪除電話的會員編號：")]) 
        for p in c.fetchall():
            phone.add_row([p[0],p[2]])
        print()
        print(phone)
        print()

        #刪除電話
        print()
        c.execute("DELETE FROM `tel` WHERE `id`=%s",[input("請輸入要刪除的電話編號：")])
        print()

        e.commit()
        e.close()
        os.system("cls") #每次執行完皆清除畫面   


    

