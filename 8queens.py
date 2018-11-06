#!/usr/bin/env python

import matplotlib.pyplot as plt

def conflict(ps,pos):
    l=len(ps)
    for i in range(l):
        if pos==ps[i] or l-i==abs(pos-ps[i]):
            #有冲突
            return True
    return False

def mou(st):
    ps=[]
    for i in st:
        ps.append(i[0])
    return ps

def queue1(num):
    st=[]
    for begin in range(num):
        #和走迷宫一样，begin是开始位置
        st.append([begin, 0])
        # 放[begin,2]表示第begin个位置，下一个位置0没有探查
        while len(st) != 0:
            ps = mou(st)
            pos, nxt = st.pop()
            for nextp in range(nxt, num):
                if not conflict(ps, nextp):
                    st.append((pos, nextp + 1))
                    st.append((nextp, 0))
                    if len(st) == num:
                        #栈的长度达到8,表示已经找到一个结果
                        ps.append(nextp)
                        yield ps
                    break
    print("搜索完毕")


def queue(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queue(num, state + (pos,)):
                    yield (pos,) + result

num=8
item=queue1(num)
a=next(item)
print(a)
plt.grid()
plt.scatter(range(num),a,800,a)
plt.title("%d皇后问题的其中一个解法"%num)
plt.show()

