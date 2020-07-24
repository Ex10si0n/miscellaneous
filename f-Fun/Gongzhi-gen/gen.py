import data
import random

arr = list(range(len(data.src)))
random.shuffle(arr)
State = input("输入批判的国家：")
City = input("输入批判的城市：")
CritisizeTarget = input("输入批判的对象：")
GongZhi = input("输入公知名字：")
Article = input("输入公知的著作：")
SocialMedia = input("输入你使用的社交媒体：")

for i in arr:
    input("Enter生成")
    print(data.src[i].format(0, State, City, CritisizeTarget, GongZhi, Article,\
                              SocialMedia))
