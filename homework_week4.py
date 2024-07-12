#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}


#取词，确定最大词长
def load_word_dict(Dict):
    dict_word = []
    max_word_length = 0
    for word in dict:
        max_word_length = max(len(word), max_word_length)
        dict_word.append(word)
    return dict_word, max_word_length

#最大词长，最小词长，遍历循环
#实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    dict_word, max_word_length = load_word_dict(Dict)
    words = []
    target = []
    for i in range(0,max_word_length): # 0,1,2,...
        #i = i + 1
        word = sentence[:i] #取第一个字
        for j in range (i, max_word_length): #1,2,...
            if word not in dict_word: #第一个字判定
                break
            else:
                words.append(word)  #在则取出
            sentence = sentence[j:] #向后移动
            word = sentence[:j]  #取下一个字，进入下一循环
            target = target.append(words)
    return target

#待切分文本
sentence = "经常有意见分歧"

all_cut(sentence, Dict)
# print(target)

#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]

