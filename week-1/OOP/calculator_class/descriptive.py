#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:15:18 2019

@author: cblessen
"""

class Calculator():
    def __init__ (self, data):
        self.data = data
    
    def length(self):
        return len(self.data)
    
    def mean(self):
        return sum(self.data)/len(self.data)
    
    def median(self):
        n = self.length()
        data_list = sorted(self.data)
        if n % 2 == 0:
            median = (data_list[n//2] + data_list[(n//2)-1])/2
            return median
        if n % 2 == 1:
            median = data_list[n//2]
            return median
    
    def variance(self):
        sample_mean = self.mean()
        calc_variance = []
        for num in self.data:
            ind_var = num - sample_mean
            squared_var = ind_var**2
            calc_variance.append(squared_var)
        total_variance = sum(calc_variance)/(len(self.data)-1)
        return total_variance
    
    def stand_dev(self):
        std_dev = self.variance()**(1/2)
        return std_dev
        
    def add_data(self, new_data):
        for num in new_data:
            self.data.append(num)
        return self.data
    
    def remove_data(self, data_to_remove):
        for num in data_to_remove:
            if num in range(len(self.data)):
                self.data.remove(num)
        return self.data
        