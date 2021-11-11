# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 01:30:15 2020

@author: Administrator
"""

import multiprocessing
import time
class myProcess(multiprocessing.Process):
    def __init__(self, index, t):
        super().__init__()
        self.index=index
        self.t=t
    def run(self):
        print('任务', self.index, '开始时间:', time.ctime())
        time.sleep(self.t)
        print('任务', self.index, '结束时间:', time.ctime())
if __name__=="__main__":	
    multiprocessing.freeze_support()		
    process1 = myProcess("A", 5)
    process2 = myProcess("B", 3)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print('总任务结束时间:', time.ctime())



