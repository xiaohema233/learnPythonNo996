# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 01:30:15 2020

@author: Administrator
"""

import multiprocessing 
import time
def task(index, t):
	print('任务', index, '开始时间:', time.ctime())
	time.sleep(t)
	print('任务', index, '结束时间:', time.ctime())
if __name__=="__main__":	
	multiprocessing.freeze_support()	 
	process1 = multiprocessing.Process(target=task,args=("A", 5))
	process1.start()
	process2 = multiprocessing.Process(target=task,args=("B", 3))
	process2.start()
	process1.join()
	process2.join()
	print('总任务结束时间:', time.ctime())
