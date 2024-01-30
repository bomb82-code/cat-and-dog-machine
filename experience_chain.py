import tensorflow as tf
import test
import catdoggenerator
import random
import threading


# argmax函数的作用是，在字典中，找出键里含outcome的项里，值最大的那项的剑值。
def argmax(my_dict={}, outcome='dog'): #输入参数是需要查询的字典，及要查询的键的关键词，在本例中关键词是“cat”还是“dog”
    checkkeys = my_dict.keys() #取字典中的所有键。

    experience_chain_outcome = {}  # 定义一个新的字典用于存放关键词对应的字典内容。
    experience_outcome = [key for key in checkkeys if outcome in key]  # 将字典的键中所有含outcome的key，拿出来作为一个集合。
    if not experience_outcome:#如果输入的根本不是经验链中的内容。
        print("This machine can't output your want! ")
    else: #输入的是经验链中有的。
        #print("experience_outcome", experience_outcome)
        for key in experience_outcome: #遍历所有键。
            # print(key)
            experience_chain_outcome[key] = my_dict[key]  # 用这个集合做索引，把字典中所有含该outcome的项拿出来作为一个新的字典。
            # print(my_dict[key])

        out = max(experience_chain_outcome,key=experience_chain_outcome.get)#取这个新字典中，值（概率）最大的键。

        print(out)#将求得的结果输出。
        print("Its probability is ", experience_chain_outcome.get(out))
        return out



current_experience_units = {}  # 存放经验单元。这个字典在经验学习和取经验中的概率最大值函数里都要用到。
experience_result = ()  # 列出本次获得的经验。
experience_num = [0, 0]  # 记录获取的经验数量，用于计算概率。


def input_thread(): #新进程函数，使得在训练的同时用户可以对经验学习提出指令。
    while True:
        user_input = input() #得到用户的输入信息。
        print("你输入的字符是:", user_input) #显示一下用户输入的信息，让用户确认。
        argmax(current_experience_units, user_input) #根据用户的信息，从经验链中找到对应的字典键中，值最大的那个。

        print("please input cat or dog do you want.")#为下一次用户输入提供指引。


def experience_learning(w):
    global current_experience_units, experience_result, experience_num

    print("please input cat or dog do you want.")#第一次提示用户的输入指引
    #for i in range(10):#那10次测试做做验证
    while True:
        past_experience_units = current_experience_units
        stimulator = random.randint(1, 2)  # 定义刺激器为随机的1或2
        #print("当前的刺激值为：", stimulator)
        outcome = catdoggenerator.generator(stimulator)  # 把刺激给猫狗机，看它输出是个啥。 catdoggenerator.generator是自定义的猫狗生成器。
        thisresult = test.recognizer(outcome)  # 把猫狗机输出的图片发到识别器中，看看它到底是个啥。test.recognizer是一个猫狗分类器。
        experience_num[stimulator - 1] += 1  # 列表的序号是从0开始的，所以要将激励减1，这个列表是记录刺激=1出现了几次，刺激=2出现了几次，并分别计算他们的概率，写入经验单元。
        #print("当前的经验数为", experience_num)

        experience_result = (stimulator, thisresult)# 本次获得的经验,刺激器与被测物输出结果的对应。
        #print("当前的经验是：", experience_result)

        keys = current_experience_units.keys()#取目前经验单元中的所有键

        for key in keys: #轮询所有键
            if stimulator not in key: #如果这次查询的key和本次的刺激不一致，那这些key对应的字典内容不要变化。
                current_experience_units[key] = past_experience_units[key]

            else:

                if experience_result != key: #虽然key中的刺激和本次一样，但是刺激产生的结果不同，那么这部分经验重新调整。论文中的Pi
                    current_experience_units[key] = (past_experience_units[key] * (
                                experience_num[stimulator - 1] - 1)) * w / (
                                                                (experience_num[stimulator - 1] - 1) * w + 1)

                else:#当前key和本次经验一致，说明本次经验的概率再次得到一个试次，将其概率调整。论文中的Pm
                    current_experience_units[experience_result] = (past_experience_units[experience_result] * (
                            experience_num[stimulator - 1] - 1) * w + 1) / ((experience_num[
                                                                                 stimulator - 1] - 1) * w + 1)

        if experience_result not in keys: #如果所有键中都没有本次的经验，说明是第一次出现，将其加入经验字典中。
            current_experience_units[experience_result] = 1 / experience_num[stimulator - 1]
        #print("当前的经验单元是", current_experience_units, "____")

    #print(current_experience_units)


if __name__ == '__main__':
    # 修改成自己测试集的文件夹路径
    w = 1  # 遗忘系数 论文中是w’
    input_thread = threading.Thread(target=input_thread) # 新开一个进程，使得在训练的同时用户可以对经验学习提出指令。
    input_thread.start()
    experience_learning(w) #运行经验学习，积攒经验。

