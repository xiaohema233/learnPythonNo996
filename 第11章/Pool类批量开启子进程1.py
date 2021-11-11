# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 01:30:15 2020

@author: Administrator
"""
import multiprocessing
import time
def task(index):
    print('任务', index[0], '开始时间:', time.ctime())
    time.sleep(index[1])
    print('任务', index[0], '结束时间:', time.ctime())
if __name__=="__main__":	
    multiprocessing.freeze_support()		
    taskList=[("A",3),("B",2),("C",1),("D",3),("E",3),
              ("F",2),("G",3),("H",2),("I",1),("J",3)]
    with multiprocessing.Pool(5) as p:
        p.map(task, taskList)







