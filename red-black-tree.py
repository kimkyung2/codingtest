# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:37:41 2022

@author: kki
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "Red"  # 신규 노드가 들어올 때는 항상 빨강
 
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.inserted_node = None
    
    # 탐색
    def find(self, data):
        return self._find_data(self.root, data)
 
    def _find_data(self, root, data):
        if root is None or root.data == data:
            return root
        elif root.data >= data:
            return self._find_data(root.left, data)
        elif root.data < data:
            return self._find_data(root.right, data)
    # 삽입
    def insert(self, data):
        self.root = self._insert_node(self.root, data, None)
        self._balancing(self.inserted_node)
        return
 
    def _insert_node(self, cur, data, parent):
        if cur is None:
            cur = Node(data)
            cur.parent = parent
            self.inserted_node = cur
        else:
            if data < cur.data:
                cur.left = self._insert_node(cur.left, data, cur)
            elif data > cur.data:
                cur.right = self._insert_node(cur.right, data, cur)
        return cur
 
    def _balancing(self, node):
        P = node.parent
        if P is None:  # 이 node가 root node이면 블랙
            node.color = "Black"
        else:  # 이 node가 root가 아닐때
            if P.color == "Red":  # parent node가 레드 일때
                G = P.parent  # 대부분 grand가 존재함, G = grand , U = uncle
                U = None
                if G.left == P:
                    U = G.right
                elif G.right == P:
                    U = G.left
 
                if U is not None and U.color == "Red":
                    # uncle이 있고 색깔이 red일때, 
                    # parent, uncle -> Black, grandparent -> Red
                    P.color, U.color = "Black", "Black"
                    G.color = "Red"
                    self._balancing(G)
                else:  # uncle이 없거나 uncle 색이 블랙일때
                    if P == G.left and P.left == node:  # LL Case
                    # 부모가 조부모의 왼쪽 자식이고, x가 부모의 왼쪽 자식일때
                        G.color, P.color = P.color, G.color
                        self._right_rotate(G)
                    elif P == G.left and P.right == node:  # LR Case
                    # 부모가 조부모의 왼쪽 자식이고, x가 부모의 오른쪽 자식일 때
                        self._left_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._right_rotate(G)
                    elif P == G.right and P.right == node:  # RR Case
                    # 부모가 조부모의 오른쪽 자식이고, x가 부모의 오른쪽 자식일 때
                        G.color, P.color = P.color, G.color
                        self._left_rotate(G)
                    elif P == G.right and P.left == node:  # RL Case
                    # 부모가 조부모의 오른쪽 자식이고, x가 부모의 왼쪽 자식일 때
                        self._right_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._left_rotate(G)
 
    def _left_rotate(self, node):
        c = node.right
        p = node.parent
 
        if c.left is not None:
            c.left.parent = node
 
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c
 
    def _right_rotate(self, node):
        c = node.left
        p = node.parent
 
        if c.right is not None:
            c.right.parent = node
 
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c
# key, 부모, 색상 출력 
def check(node):
    if node.left is not None:
        check(node.left)
    if node.parent != None:
        print(
            f'key: {node.data}, parent: {node.parent.data}, color: {node.color}')
    else:
        print(f'key: {node.data}, root: {node.parent}, color: {node.color}')
    if node.right is not None:
        check(node.right)
 
rbt = RedBlackTree()
a = [2, 1, 8, 9, 7, 3, 6, 4, 5]
 
for x in a:
    rbt.insert(x)
 
check(rbt.root)
print()