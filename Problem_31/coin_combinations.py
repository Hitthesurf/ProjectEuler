#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:26:23 2019

@author: pi
"""
import math
import time
    
class number_permutations():
    def __init__(self, only_numbers = []):
        self.only_numbers = only_numbers.sort()
        self.current_perm = []
        self.current_num = 0
        self.count_perms = 0
        self.permutation = []
        self.max_base = []
        
    def refresh(self):
        self.current_perm = []
        self.current_num = 0
        self.count_perms = 0
        self.permutation = []
        self.max_base = []
        
    def work_out_base(self):
        self.max_base = []
        for base in self.only_numbers:
            num = self.current_num/base
            if num < 1:
                num = 0
            elif num > 1:
                num = math.ceil(num)
            self.max_base.append(num)
        
    def make_number(self):
        num_array = []
        for i in range(0, len(self.only_numbers)):
            num_array.append(0)
        self.current_perm = num_array
    
    def add_numbers(self):
        total = 0
        for index in range(0, len(self.only_numbers)):
            base = self.only_numbers[index]
            number = self.current_perm[index]
            total += number * base
        return total
    
    def add_perm(self):
        local_current_perm = self.current_perm[:] #take by value
        if self.permutation.count(local_current_perm) == 0:
            self.permutation.append(local_current_perm)
            self.count_perms +=1
            
    def next_number(self):
        for i in range(len(self.current_perm) - 1, -1, -1):
            view_num = self.current_perm[i]
            if self.max_base[i] > view_num:
                self.current_perm[i] += 1
                if self.add_numbers()-1 > self.current_num:
                    self.current_perm[i] += (self.max_base[i] - view_num)-1
                break
            else:
                self.current_perm[i] = 0

    def perm_number(self, num):
        self.refresh()
        start_time = time.time()
        self.current_num = num
        self.work_out_base()
        self.make_number()
        while self.current_perm != self.max_base:            
            if self.add_numbers() == num:
                self.add_perm()
            self.next_number()
        end_time = time.time()
        print (str(end_time-start_time))
        
    def show_permutations(self):
        string = ""
        for perm in self.permutation:       
            for index in range(0, len(perm)):
                string += str(perm[index]) + "x"
                string += str(self.only_numbers[index]) + " "
            string += "\n"
        return string
            
            
            
            
            
            
            