import threading,queue,time,random
class myThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while not self.queue.empty():
            index = self.queue.get()
            print(index)
            print('任务', index, '开始时间:', time.ctime())
            time.sleep(random.randint(0,3))
            print('任务', index, '结束时间:', time.ctime())
            self.queue.task_done()
queue = queue.Queue()
taskList=["A","B","C","D","E","F","G","H","I","J"]
for task in taskList:
    queue.put(task)
for i in range(5):
    thread = myThread(queue)
    thread.setDaemon(True)
    thread.start()
queue.join()
print('总任务结束时间:', time.ctime())
