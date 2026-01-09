class Solution:
    def exclusiveTime(self, n: int, logs:[str]) -> [int]:
        #n个进程
        res=[0]*n
        stack=[]

        for i in logs:
            #得到每个元素
            idx = int(i.split(':')[0])
            typ = i.split(':')[1]
            ts = int(i.split(':')[2])

            if typ == 'start':
                if stack:
                    top_idx, top_start = stack[-1]
                    res[top_idx] += ts - top_start
                stack.append((idx, ts))  # 新任务必须压栈
            else:  # end
                top_idx, top_start = stack.pop()
                res[top_idx] += ts - top_start + 1
                if stack:  # 弹栈后若还有任务，更新其恢复点
                    stack[-1] = (stack[-1][0], ts + 1)

        return  res



"""
日志按时间顺序给出，同一时刻只能有一个函数占用 CPU。
因此：
遇到 start：如果栈非空，说明旧函数被中断了，栈顶那个就是唯一被中断的函数；
遇到 end：弹出的就是当前正在运行的函数，弹完后如果栈里还有元素，那它一定是刚刚被中断、现在马上要恢复的那个函数，也只有一个。

同一个函数（同一个 idx）可以在还没返回的时候又被再次调用，所以在碰到start的情况时我们选择访问栈里的元素，pop出来的会会丢失进程
"""
