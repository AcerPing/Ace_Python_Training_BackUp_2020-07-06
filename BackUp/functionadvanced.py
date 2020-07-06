# def x(a=2,b=8):
#     print(a**b)
#     return a+b
# z=x(b=2)
# print(z)

# def z(B,E):
#     print(B**E)
# z(3,3)

def ave(*n):
    sum=0
    for x in n:
        sum=sum+x
    avg=sum/len(n)
    print(avg)
    return x
ave(3,6,9,10)
