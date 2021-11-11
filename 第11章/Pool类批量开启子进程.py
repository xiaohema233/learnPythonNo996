# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 01:30:15 2020

@author: Administrator
"""
import multiprocessing
import time
def task(index):
    print('任务', index, '开始时间:', time.ctime())
    time.sleep(1)
    print('任务', index, '结束时间:', time.ctime())
if __name__=="__main__":	
    multiprocessing.freeze_support()		
    taskList=["A","B","C","D","E","F","G","H","I","J"]
    with multiprocessing.Pool(5) as p:
        p.map(task, taskList)




