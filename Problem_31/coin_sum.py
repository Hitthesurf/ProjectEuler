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

def combine(array_1, array_2): ##only works for multiples of only_numbers
    master_array = []
    for select in range(0, len(array_1)):
        for join_to in range(0, len(array_2)):
            temp_array = array_1[select] + array_2[join_to]
            temp_array.sort()
            master_array.append(temp_array)
            
    return delete_duplicates(master_array)

          
def delete_duplicates(array):
    no_duplicates = []
    for i in range(0,len(array)):
        if no_duplicates.count(array[i]) == 0:
            no_duplicates.append(array[i])
    return no_duplicates

    
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
        
    def max_number(self):
        largest = 1
        max_num = []
        for i in range(0,self.current_num):
            max_num.append(largest)
        return max_num
        
    def make_number(self):
        smallest = self.only_numbers[0]
        for i in range(0,self.current_num):
            self.current_perm.append(smallest)
    
    def add_perm(self):
        local_current_perm = self.current_perm[:] #take by value
        local_current_perm.sort()
        if self.permutation.count(local_current_perm) == 0:
            print(self.current_perm)
            self.permutation.append(local_current_perm)
            self.count_perms +=1
            
    def inc_combine(self, array_1, array_2):
        master_array = combine(array_1, array_2)
        if self.only_numbers.count(len(master_array[0])) == 1:
            temp_array = []
            temp_array += [0] * (len(master_array[0])-1)
            temp_array += [len(master_array[0])]
            master_array.append(temp_array)
        return master_array
    
    def perm_number(self, num):
        self.refresh()
        self.current_num = num
        self.make_number()
        max_num = self.max_number()
        while self.current_perm != max_num:
            #print (self.current_perm)
            total = add_numbers(self.current_perm)
            if self.current_num == total:
                self.add_perm()
            self.next_number()
            
        if self.check_num():
            self.add_perm()


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
    