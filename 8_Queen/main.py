import random
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
        #这里用两个点之差算横坐标，不能等于纵坐标的差。来确保对角线问题。
            return True
    return False

def queens(num, state=()): 

    for pos in range(num):
        if not conflict(state, pos):#这个if是没有else的，因为当跑到conflict那里为真的时候，层层stack就被返上来，取消掉了整个这组排列（也就是没结果）
            if len(state) == num-1:
                yield (pos, )
            else:
            #这里多种组合分叉着走，也是遍历的关键。
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

if __name__ == "__main__":
   print(list(queens(8)))
   prettyprint(random.choice(list(queens(8)))) 
   #if main以上的部分其实是把所有皇后布阵都给出来了，random.choice是选择了其中一个list 去打印。
