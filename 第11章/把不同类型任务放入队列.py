import threading,queue
import time
class myThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            if self.queue.qsize() > 0:
                method, para1,para2 = self.queue.get()
                method(para1,para2)
                self.queue.task_done()
def task1(index, t):
    print('task1任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('task1任务', index, '结束时间:', time.ctime())
def task2(index, t):
    print('task2任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('task2任务', index, '结束时间:', time.ctime()) 
def task3(index, t):
    print('task3任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('task3任务', index, '结束时间:', time.ctime())  
queue = queue.Queue()
taskList=[(task1,"A",3),(task2,"B",2),(task3,"C",1),(task1,"D",3),(task1,"E",3),
(task2,"F",2),(task3,"G",1),(task2,"H",3),(task1,"I",3), (task2,"J",2),]
for item in taskList:
    queue.put(item)
for i in range(5):
    thread = myThread(queue)
    thread.setDaemon(True)
    thread.start()
queue.join()
print('总任务结束时间:', time.ctime())
