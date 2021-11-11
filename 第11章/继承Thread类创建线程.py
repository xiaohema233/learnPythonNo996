import threading
import time
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__(target=func, name=name,args=args)
    def run(self):
        self._target(*self._args)
def task(index, t):
    print('任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('任务', index, '结束时间:', time.ctime())
thread1 = MyThread(task,("A", 5))
thread2 = MyThread(task,("B", 3))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('总任务结束时间:', time.ctime())
