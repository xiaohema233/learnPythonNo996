# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:38:25 2020

@author: Administrator
"""
__all__=["Kid","speak_obj"]
class Person:
    def __init__(self,name,age,like):
        self.name = name
        self.age = age
        self.like = like
    def eat(self):
        print(self.name+"开始吃饭!-pack")
    def speak(self):
        print("%s说: 我%d岁了，我爱好%s。-pack" % (self.name, self.age, self.like))
class Kid(Person):
    def speak(self):
        print("我在上幼儿园！-pack")
def speak_obj(obj):
    obj.speak()
NUMBER=1000

