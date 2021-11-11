import threading,time
def task(index, t):
    print('任务', index, '开始时间:', time.ctime())
    time.sleep(t)
    print('任务', index, '结束时间:', time.ctime())
task("A", 5)
task("B", 3)
print('总任务结束时间:', time.ctime())
