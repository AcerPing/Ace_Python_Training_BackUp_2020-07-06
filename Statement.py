#隨機選取
# import random
# data=random.choice([1,4,6,8,10])
# print(data)

#隨機選取
# import random
# data=random.sample([1,4,6,8,10],4)
# print(data)

#Shuffle 洗牌 隨機調換順序
# data=[1,5,10,20,25]
# import random
# random.shuffle(data)
# print(data)

#取得隨機亂數 0~1之間
# import random
# data=random.random()
# print(data)

#取得隨機亂數 
# import random
# data=random.uniform(20,180)
# print(data)

#常態分配
# 平均數100,標準差5,得到的資料多數落於95~105之間
# import random
# data=random.normalvariate(100,5)
# print(data)

#統計
#取平均數
import statistics
average=statistics.mean([1,4,5,10])
print(average)
#取中位數
middle=statistics.median([1,4,5,10])
print(middle)
#取標準差
StandardDeviation=statistics.stdev([1,4,5,10])
print(StandardDeviation)

