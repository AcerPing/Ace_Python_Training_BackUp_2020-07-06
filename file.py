# file=open("HelloAce.txt",mode="w",encoding="utf-8") #開啟檔案
# file.write("Hello\tMountaineering\n") #撰寫檔案
# file.write("Becareful\nHiking\n")
# file.write("奇萊東稜\t快點決定")
# file.close() #關閉檔案

# with open("HelloAce.txt",mode="w",encoding="utf-8") as file:
#     file.write("奇萊東稜\n奮鬥奮鬥再奮鬥") 
# #with open 會自動安全關閉檔案

# #讀取檔案
# with open("HelloAce.txt",mode="r",encoding="utf-8") as file:
#     datum=file.read()
# print(datum)

# with open("AceSummary.txt",mode="w",encoding="utf-8") as file:
#     file.write("6\n7\n8\n9\n10")

sum=0
with open("AceSummary.txt",mode="r",encoding="utf-8") as file:
    for x in file: #一行一行的讀取出來
        x=int(x)
        sum=sum+x
print(sum)  

# print(data)
    # data=file.read()
    # data=int(data)
