import threading
import time
def task(index, t):
    print('任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('任务', index, '结束时间:', time.ctime())
thread1 = threading.Thread(target=task,args=("A", 5))
thread1.start()
thread2 = threading.Thread(target=task,args=("B", 3))
thread2.start()
thread1.join()
thread2.join()
print('总任务结束时间:', time.ctime())
