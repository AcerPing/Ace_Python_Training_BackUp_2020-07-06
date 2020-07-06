#定義類別與類別屬性
#封裝在類別中的變數與函式

# 定義一個類別，叫做Student，並且有三個屬性，分別為S1、S2及read
# class Student:
#     S1=["name","email"]
#     S2=["name","email"]
#     def calculator(a,b):
#         print(a+b)
#         return "Error"
#     def nation(country):
#         print("from",country)
#         return "Not on the Earth"
#     def individual(personal):
#         if personal not in Student.S1:
#             print("not required")
#         else:
#             print("write it down")
# #呼叫(使用類別)
# print(Student.S1)
# print(Student.S2)
# Student.calculator(a=5,b=10)
# Student.nation("Japan")
# Student.individual("number")

# 實體物件的設計
# class Position:
#     def __init__(self,x,y):
#         self.X=x**2
#         self.Y=y**2
# # 定義實體方法
#     def show_info(self):
#         print(self.X,self.Y)
#     def length(self,objectA,objectB):
#         print(((self.X-objectA)**2+(self.Y-objectB)**2)**0.5)

# #建立實體物件
# Location1=Position(15,20)
# print(Location1.X)
# print(Location1.Y)
# Location1.show_info() #呼叫實體方法
# Location1.length(30,45)

# Location2=Position(21,35)
# print(Location2.X)
# print(Location2.Y)
# Location2.show_info()
# Location2.length(55,25)

# Position(25,20).show_info()
# Position(25,20).length(14,15)

# class Student:
#     def __init__(self,Name,Family):
#         self.FirstName=Name
#         self.LastName=Family
#     #定義實體方法
#     def show_info(self):
#         print(self.FirstName,self.LastName)

# S1=Student(Name="Ace",Family="Ho")
# print(S1.FirstName)
# print(S1.LastName)
# S1.show_info()
# # S2=Student("Ho","Ace")
# # print(S2.FirstName)
# # print(S2.LastName)
# S3=Student("Che","Ping")
# print(S3.FirstName)
# print(S3.LastName)
# S3.show_info()
# # S4=Student("ChePing","Ho")
# # print(S4.FirstName)
# # print(S4.LastName)
# Student("人可","一郎").show_info()

# with open("AceSummary.txt",mode="w",encoding="utf-8") as file:
#     file.write("6\n7\n8\n9\n10")

# def function(a,b):
# 	a+b
# 	return a**b
# print(function(5,3))

class File:
    #初始化
    def __init__(self,folder):
        self.fold=folder
    #定義實體方法
    def open(self):
        self.open=open(self.fold,mode="r",encoding="utf-8")
    def read(self):
        return self.open.read()

# F1=File("data.txt")
# F1.open()
# D1=F1.read()
# print(D1)

# class File:
#     def __init__(self,file):
#         self.file=file
#     def open(self):
#         self.upload=open(self.file,mode="r")
#     def read(self):
#         return open(self.file,mode="r").read()
    
F2=File("AceSummary.txt")
F2.open()
D2=F2.read()
print(D2)


# F2=File("AceSummary.txt")
# F2.open()
# D2=F2.read()
# print(D2)

# print(File("data.txt").read())


