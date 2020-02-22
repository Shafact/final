"""
【问题描述】

高级猜数字

制作交互性强、容错率高的猜数字游戏程序。

要求：

为猜数字游戏增加记录玩家成绩的功能，包括玩家用户名、玩的次数和平均猜中的轮数等；
如果记录里没有玩家输入的用户名，就新建一条记录，否则在原有记录上更新数据；
对玩家输入做检测，判定输入的有效性，并保证程序不会因异常输入而出错；
从网络上获取每一局的答案，请求地址：https://python666.cn/cls/number/guess/


"""

""" Plans
1. 设定一个dictionary，包含每个用户的信息，读出原始文件的数据
2. 创建一个用户类，包含用户的名字，猜数字的方法，用户玩的轮数，最少用了多少次猜中，平均每轮猜的次数
3. 每个玩家输入名字后，检测是否已有数据，有就把这些已有数据pass到类上，没有就不用pass按原来的来
4. 最后将dictionary的值存在列表里，每行一次输出
"""
import requests

#定义一个函数，读出原始数据
def read_file(path):
    with open(path) as f:
        l = [i.split() for i in f.readlines()]
        for i in range(1, len(l)):
            for j in range(1, len(l[0])):
                l[i][j] = int(l[i][j])
        return l
#定义一个函数，将原始数据录入用户数据字典
def add_original(ls):
    global all_records
    for i in ls:
        all_records[i[0]] = i

#定义一个用户类，含有用户名，用户玩的轮数，最少用了多少次猜中，平均多少次猜中
class GamePlayer:
    def __init__(self, name='', total_round=0, best_times=0, total_times=0):
        self.name = name
        self.total_round = total_round
        self.best_times = best_times
        self.total_times = total_times

    #定义猜数字的程序, 返回一个列表
    def guess_num(self):
        req = requests.get('https://python666.cn/cls/number/guess/')
        num = int(req.text)
        print(num, type(num))

#test class
sharon = GamePlayer('Sharon')
sharon.guess_num()


#读出原始数据
original_records = read_file('game_many_users.txt')
print("original_records: ", original_records)

#定义一个dictionary， 储存所有用户数据
all_records = {}

#将原始数据加入字典
add_original(original_records)
print('all records: ',all_records)

#main process:
#建立用户类

user = input("Please enter your name: ")

#检测user是否已经有record了, 有则把已有数据pass到类上，没有就保持新类
print(user in all_records)
if user in all_records:
    player = GamePlayer(user,total_round=all_records[user][1], best_times=all_records[user][2], total_times=all_records[user][3])
else:
    player = GamePlayer(user)
print(player.name,player.total_round,player.best_times,player.total_times)
