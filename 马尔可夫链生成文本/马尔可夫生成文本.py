#简单使用马尔科连生成文本

#作为文本生成器，可以输入任何文本，让他生成相似的句子
model={}


#读取文本文件中的句子，并按照规则进行划分
file=open('data.txt')
for line in file:
    line=line.lower().split()
    for i,word in enumerate(line):
        if i==len(line)-1:
            model['END']=model.get('END',[])+[word]
        else :
            if i==0:
                model['START']=model.get('START',[])+[word]
            model[word]=model.get(word,[])+[line[i+1]]

import random
#生成器
generted=[]
while True:
    if not generted:
        words=model['START']
    elif generted[-1] in model['END']:
        break
    else:
        words=model[generted[-1]]
    generted.append(random.choice(words))

for i in generted:
    print(i,end = " ")