# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:37:41 2022

@author: kki
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right = None
        self.left = None
        self.color = "RED" # 신규 노드가 들어올 때는 항상 빨강
        
class RBT:
    def __init__(self):
        self.root = None
        self.insert_node = None
    
    # 삽입
    def insert(self, data):
        self.root = self.insert_value(self.root, data, None)
        self.balancing(self.insert_node)
    
    def insert_value(self, node, data, parent):
        if node is None:
            node = Node(data)
            node.parent = parent
            self.insert_node = node
        else:
            if data < node.data:
                node.left = self.insert_value(node.left, data, node)
            else:
                node.right = self.insert_value(node.right, data, node)
        return node
    
    def balancing(self, node):
        P = node.parent
        if P is None: # 이 node가 root node이면 블랙
            node.color = "Black"
            
        else: # 이 node가 root가 아닐때
            if P.color == "Red": # parent node가 레드일 때
                grand = P.parent # 대부분 grand가 존재함
                uncle = None 
                if grand.left == P:
                    uncle = grand.right
                elif grand.right == P:
                    uncle = grand.left
                    
                if uncle != None and uncle == "Red": # uncle이 none이 아니고 색이 red 일때
                    P.color = "Black"
                    uncle.color = "Black"
                    grand.color = "Red"
                    self.balancing(grand) # 조부모 노드로 치환 후 다시 반복(?)
                else: # uncle이 없거나 uncle 색이 블랙일 때
                    if P == grand.left and P.left ==node:
                        # 부모가 조부모의 왼쪽 자식이고 , x가 부모의 왼쪽 자식일 때 (LLCase)
                        grand.color, P.color = P.color, grand.color
                        self.right_rotate(grand)
                    elif P == grand.left and node == P.right:
                        # 부모가 조부모의 왼쪽 자식이고, x가 부모의 오른쪽 자식일 때 (LRCase)
                        self.left_rotate(P)
                        grand.color, node.color = node.color, grand.color
                        self.right_rotate(grand)
                    elif P == grand.right and node == P.right:
                        # 부모가 조부모의 오른쪽 자식이고, x가 부모의 오른쪽 자식일 때 (RRCase)
                        grand.color, P.color = P.color, grand.color
                        self.left_rotate(grand)
                    elif P == grand.right and node == P.left:
                        # 부모가 조부모의 오른쪽 자식이고, x가 부모의 왼쪽 자식일 때 (RLCase)
                        self.right_rotate(P)
                        grand.color, node.color = node.color, grand.color
                        self.left_rotate(grand)
    
    def right_rotate(self, node):
        c = node.right
        p = node.parent
        
        if c.left != None:
            c.left.parent = node
        
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
                    

    
    # 탐색
    def find(self, data):
        return self._find_data(self.root, data)
    
    def _find_data(self, root, data):
        if root is None or root.data == data:
            return root
        elif data > root.data:
            return self._find_data(self.right, data)
        else:
            return self._find_data(self.left, data)
        
    