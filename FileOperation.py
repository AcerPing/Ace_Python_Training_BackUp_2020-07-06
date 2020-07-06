#令X為None
x=None
#當x不等於0時，列印出目錄選單
while x!="0":
    import os
    dir = os.getcwd()
    print("工作路徑：",dir)
    print("(0) 離開程式")
    print("(1) 列出檔案")
    print("(2) 列出資料夾")
    print("(3) 顯示檔案內容")
    print("(4) 刪除檔案")
    print("(5) 執行檔案")
    print("(6) 進入資料夾")
    print("(7) 刪除資料夾")
    print("(8) 回上層資料夾")
    #輸入x資料
    x=input("操作:")
    #取得資料夾內的檔案列表
    Z=os.listdir("./")
    #另fileList為檔案列表，dirList為資料夾列表
    fileList=[]
    dirList=[]
    #當判斷為檔案時，加到檔案列表，否則加到資料夾列表
    for D in Z:
        if os.path.isdir(D)!=True:
            fileList.append(D) #採用append加入
            fileList.sort()
            # fileList=fileList+[D]
        else:
            dirList.append(D) #採用append加入
            dirList.sort()
            # dirList=dirList+[D]
    
    #(1) 列出檔案
    if x=="1":
        print("\n")
        print("================ファイル（檔案列表）================")
        for I in range(0,len(fileList),1):
            print(I,fileList[I])
        print("\n")
    
    #(2) 列出資料夾
    elif x=="2":
        print("\n")
        print("================カタログ（資料夾列表）================")
        for I in range(0,len(dirList),1):
            print(I,dirList[I])
        print("\n")

    #(3) 顯示檔案內容
    elif x=="3":
        print("\n")
        print("================ファイル（檔案列表）================")
        for I in range(0,len(fileList),1):
            print(I,fileList[I])
        print("")

        P=input("入力してください（請輸入檔案索引）：")
        os.system("cls")
        print("\n")
        print("================始まり（檔案開始）================")
        import codecs
        with codecs.open(fileList[int(P)],"rb","utf-8") as F:
            print(F.read())
        print("================おしまい（檔案結束）================")
        print("\n")
    
    # (4) 刪除檔案
    elif x=="4":
        print("\n")
        print("================ファイル（檔案列表）================")
        for I in range(0,len(fileList),1):
            print(I,fileList[I])
        print("")    
        P=input("入力してください（請輸入檔案索引）：")
        import os
        os.remove(fileList[int(P)])
        os.system("cls")

    #(5) 執行檔案
    elif x=="5":
        print("\n")
        print("================ファイル（檔案列表）================")
        for I in range(0,len(fileList),1):
            print(I,fileList[I])
        print("")    
        P=input("入力してください（請輸入檔案索引）：")
        import webbrowser
        webbrowser.open(fileList[int(P)],new=0, autoraise=True)
        os.system("cls")

    #(6) 進入資料夾
    elif x=="6":
        print("\n")
        print("================カタログ（資料夾列表）================")
        for I in range(0,len(dirList),1):
            print(I,dirList[I])
        print("\n")
        P=input("入力してください（請輸入資料夾索引）：")
        os.system("cls")
        # Y=os.path.dirname(os.getcwd()+"./"+dirList[int(P)])
        # print(dir+"\\"+dirList[int(P)])
        os.chdir((dir+"\\"+dirList[int(P)]))
        # print(os.path.dirname(dir+"\\"+dirList[int(P)]))
        # os.chdir(Y)
    
    #(7) 刪除資料夾
    if x=="7":
        print("\n")
        print("================カタログ（資料夾列表）================")
        for I in range(0,len(dirList),1):
            print(I,dirList[I])
        print("\n")
        P=input("入力してください（請輸入資料夾索引）：")
        #os.rmdir(dirList[int(P)])→刪除指定的資料夾
        os.rmdir(dirList[int(P)])
        os.system("cls")
        
    #(8) 回上層資料夾
    elif x=="8":
        # print(os.getcwd())
        # print(os.path.dirname(os.getcwd()))
        #os.path.dirname→傳回路徑字串中的路徑部分
        Y=os.path.dirname(os.getcwd())
        #os.chdir→改變工作路徑
        os.chdir(Y)

    #當輸入的指令為0時，清除畫面，並中斷迴圈
    if x=="0":
        os.system("cls")
        break


    # if x=="1":
    #     y=os.listdir(os.getcwd())
    #     t=0
    #     for z in y:
    #         if os.path.isfile(z)==True: 
    #             print(t,z)
    #             t=t+1
    # elif x=="2":
    #     y=os.listdir(os.getcwd())
    #     t=0
    #     for z in y:
    #         if os.path.isdir(z)==True:
    #             print(t,z)
    #             t=t+1
    # elif x=="3":
    #     y=os.listdir(os.getcwd())
    #     t=0
    #     for z in y:
    #         if os.path.isfile(z)==True: 
    #             print(t,z)
    #             t=t+1
    #     i=input("請輸入檔案索引：")
    #     # dic=
    #     import codecs
    #     f=codecs.open(argv[1],"rb","utf-8")
    #     g=f.read()
    #     print(g)


    #     print("(3) 顯示檔案內容")
    # elif x=="4":
    #     print("(4) 刪除檔案")
    # if x=="0":
    #     import os
    #     os.system("cls")

 #TODO x!="0"
 #  while x!="0":
    # import os
    # print("工作路徑：",os.getcwd())
    # print("(0) 離開程式")
    # print("(1) 列出檔案")
    # print("(2) 列出資料夾")
    # print("(3) 顯示檔案內容")
    # print("(4) 刪除檔案")
    # print("(5) 執行檔案")
    # print("(6) 進入資料夾")
    # print("(7) 刪除資料夾")
    # print("(8) 回上層資料夾")
    # x=input("操作:")