#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:03:15 2019

@author: pi
"""
import multiprocessing as mult
import time
import math

def is_prime(num):
    if num == 2:
        return True
    if num%2 == 0:
        return False
    for i in range(3,math.ceil(math.sqrt(num))+1,2):
         if num%i == 0:
             return False
    if num == 1:
        return False  
    return True


def prime_at(index):
    start_time = time.time()
    counter = 0
    i = 1
    while True:
        if is_prime(i):
            counter += 1
            if counter == index:
                end_time = time.time()
                print(str(end_time - start_time))
                return i
        i += 1
    
        
def prime_workout(start, stop_at, step, queue):
    #counter = 0
    i = start
    prime_array = []
    while i < stop_at:
        if is_prime(i):
            #counter += 1
            prime_array.append(i)
            queue.put(i)
        i += step
    return prime_array

def mult_prime_core(numbers, cores = 0):
    start_time = time.time()
    prime_que = mult.Queue()
    prime_array = [2]
    if cores == 0:
        cores = mult.cpu_count()
    step = cores * 2
    stop_at = numbers*step
    start = []
    Proc = []
    for i in range(0, cores):
        start.append(2*i + 1)
        Proc.append(mult.Process(target=prime_workout, args=(start[i],stop_at,step, prime_que)))
    for i in Proc:
        i.start()
    while prime_que.empty() is False:
        prime_array.append(prime_que.get())
    for i in Proc:
        i.join()
    
    while prime_que.empty() is False:
        prime_array.append(prime_que.get())
    prime_array.sort()
    end_time = time.time()
    print(prime_array[-1])
    print(prime_array[0:10])
    print(len(prime_array))
    if len(prime_array)>10000:
        print(prime_array[10000])
        pass
    print (str(end_time - start_time))
        