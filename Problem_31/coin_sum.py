#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:17:19 2019

@author: pi
"""
def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

    
class number_permutations():
    def __init__(self, only_numbers = []):
        self.only_numbers = only_numbers.sort()
        self.current_perm = []
        self.current_num = 0
        self.count_perms = 0
        self.permutation = []
        
    def refresh(self):
        self.current_perm = []
        self.current_num = 0
        self.count_perms = 0
        self.permutation = []     
        
    def make_number(self):
        smallest = self.only_numbers[0]
        for i in range(0,self.current_num):
            self.current_perm.append(smallest)
        
    
    def add_perm(self):
        local_current_perm = self.current_perm[:] #take by value
        local_current_perm.sort()
        if self.permutation.count(local_current_perm) == 0:
            self.permutation.append(local_current_perm)
            self.count_perms +=1
    
    def perm_number(self, num):
        self.refresh()
        self.current_num = num
        self.make_number()
        for i in range(0,len(self.only_numbers)**num):
            if self.check_num():
                self.add_perm()
            self.next_number()
    
    def next_number(self):
        for i in range(len(self.current_perm) - 1, -1, -1):
            view_num = self.current_perm[i]
            if self.only_numbers[-1] > view_num:
                index = self.only_numbers.index(view_num)
                self.current_perm[i] = self.only_numbers[index + 1]
                break
            else:
                self.current_perm[i] = self.only_numbers[0]
                
            
    def check_num(self):
        if self.current_num == add_numbers(self.current_perm):
            return True
        else:
            return False
    