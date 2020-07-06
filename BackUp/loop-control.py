# n=0
# while n<5: 
#     if n==3:
#         break
#     print(n)
#     n=n+1
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     x=x+1
# print("結束",x)
# sum=0
# for x in range(11):
#     sum=sum+x
# else:
#     print(sum)
# print(9**0.5)
# x=input("請輸入數字:")
# x=int(x)
# for y in range(x+1):
#     if y*y==x:
#         print(y)
#         break
# else:
#     print("無法滿足")
x=input("請輸入數字:")
x=int(x)
if x**0.5%1==0:
    print("開根號",x**0.5)
else:
    print("無法滿足")