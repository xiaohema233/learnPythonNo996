import threading
import time,random
class myThread(threading.Thread):
    def __init__(self, index, t):
        super().__init__()
        self.index=index
        self.t=t
    def run(self):
        print('任务', self.index, '开始时间:', time.ctime())
        time.sleep(self.t)
        print('任务', self.index, '结束时间:', time.ctime())
taskList=["A","B","C","D","E","F","G","H","I","J"]
threadList =[]
for i in taskList:
    threadList.append(myThread(i,random.randint(0,3)))
for item in threadList:
    item.start()
for item in threadList:
    item.join()
print('总任务结束时间:', time.ctime())
