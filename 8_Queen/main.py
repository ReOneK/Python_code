import random
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):   #确保相同行和对角线没有皇后
            return True
    return False

def queens(num, state=()): 

    for pos in range(num):          #遍历所有列，然后在确保每一列的每一行和对角线无皇后
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos, )
            else:
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
