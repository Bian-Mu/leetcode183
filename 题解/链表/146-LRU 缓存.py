# https://leetcode.cn/problems/lru-cache/
# Source: https://walkccc.me/LeetCode/problems/146/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Node:
  def __init__(self, key: int, value: int):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None


class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.keyToNode = {}
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.join(self.head, self.tail)

  def get(self, key: int) -> int:
    if key not in self.keyToNode:
      return -1

    node = self.keyToNode[key]
    self.remove(node)
    self.moveToHead(node)
    return node.value

  def put(self, key: int, value: int) -> None:
    if key in self.keyToNode:
      node = self.keyToNode[key]
      node.value = value
      self.remove(node)
      self.moveToHead(node)
      return

    if len(self.keyToNode) == self.capacity:
      lastNode = self.tail.prev
      del self.keyToNode[lastNode.key]
      self.remove(lastNode)

    self.moveToHead(Node(key, value))
    self.keyToNode[key] = self.head.next

  def join(self, node1: Node, node2: Node):
    node1.next = node2
    node2.prev = node1

  def moveToHead(self, node: Node):
    self.join(node, self.head.next)
    self.join(self.head, node)

  def remove(self, node: Node):
    self.join(node.prev, node.next)

class MySolution:
  def __init__(self,capacity:int) -> None:
    self.capacity=capacity
    self.head=Node(-1,-1)
    self.tail=Node(-1,-1)
    self.connect(self.head,self.tail)
    self.map={}
    
  def connect(self,n1:Node,n2:Node):
    n1.next=n2
    n2.prev=n1
  
  def get(self,key:int)->int:
    if key not in self.map:
      return -1
    
    node=self.map[key]
    self.remove(node)
    self.addToHead(node)
    return node.value
    
  def put(self,key:int,value:int)-> None:
    if key in self.map:
      node=self.map[key]
      node.value=value
      self.remove(node)
      self.addToHead(node)
      
    else:
      node=Node(key,value)
      self.map[key]=node
      self.addToHead(node)
    
      if len(self.map)>self.capacity:
        lastNode=self.tail.prev
        self.connect(lastNode.prev,self.tail)
        del self.map[lastNode.key]
  
  def addToHead(self,node)->None:
    self.connect(node,self.head.next)
    self.connect(self.head,node)
    
  def remove(self,node)->None:
    self.connect(node.prev,node.next)
    