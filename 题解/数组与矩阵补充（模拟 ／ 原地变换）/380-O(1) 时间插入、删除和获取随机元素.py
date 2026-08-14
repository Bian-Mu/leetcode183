# https://leetcode.cn/problems/insert-delete-getrandom-o1/
# Source: https://walkccc.me/LeetCode/problems/380/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
import random

class RandomizedSet:
  def __init__(self):
    self.vals = []
    self.valToIndex = collections.defaultdict(int)  # {val: index in vals}

  def insert(self, val: int) -> bool:
    if val in self.valToIndex:
      return False
    self.valToIndex[val] = len(self.vals)
    self.vals.append(val)
    return True

  def remove(self, val: int) -> bool:
    if val not in self.valToIndex:
      return False
    index = self.valToIndex[val]
    # The order of the following two lines is important when vals.size() == 1.
    self.valToIndex[self.vals[-1]] = index
    del self.valToIndex[val]
    self.vals[index] = self.vals[-1]
    self.vals.pop()
    return True

  def getRandom(self) -> int:
    index = random.randint(0, len(self.vals) - 1)
    return self.vals[index]

class mysolution:
  def __init__(self):
    self.vals=[]
    self.map={}
  
  def insert(self,val:int)->bool:
    if val in self.map:
      return False
    
    self.map[val]=len(self.vals)
    self.vals.append(val)
    return True
  
  def remove(self,val:int)->bool:
    if val not in self.map:
      return False
    
    lastV=self.vals[-1]
    i=self.map[val]
    
    self.vals[i]=lastV
    self.vals.pop()
    self.map[lastV]=i
    self.map.pop(val)
    
    return True
  
  def getRandom(self)->int:
    index=random.randint(0,len(self.vals)-1)
    return self.vals[index]