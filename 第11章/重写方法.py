import threading
import time
class myThread(threading.Thread):
    def __init__(self, index, t):
        super().__init__()
        self.index=index
        self.t=t
    def run(self):
        print('任务', self.index, '开始时间:', time.ctime())
        time.sleep(self.t)
        print('任务', self.index, '结束时间:', time.ctime())
thread1 = myThread("A", 5)
thread2 = myThread("B", 3)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('总任务结束时间:', time.ctime())
