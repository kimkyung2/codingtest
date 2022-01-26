# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:56:56 2022

@author: kki
"""

# 노드 생성
class Node:
    def __init__(self, value):
        self.value = value
        # 자식노드가 없으므로 left랑 right에 값을 None으로 넣어줌
        self.left = None 
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root
    # 노드 삽입    
    def insert(self, value):
        # current_node를 루트 노드로 초기화
        self.current_node = self.root
        
        while True:
            # 삽입하고자 하는 값이 current_node 값보다 작을 때 현재 노드의 왼쪽 자식 노드가 있는지 확인하고 있으면 current_node를 갱신함.
            # 없을 경우에는 current_node의 왼쪽 자식 노드에 삽입하고자 하는 노드 삽입
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            # 삽입하고자 하는 값이 current_node 값보다 클때는 작을때의 경우의 반대로 구현
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 노드 탐색
    def search(self, value):
        # 루트 노드부터 탐색 시작
        self.current_node = self.root
        while self.current_node:
            # current_node 값이 찾고자 하는 경우 true를 리턴
            if self.current_node.value == value:
                return True
            # current_node 값이 찾고자 하는 값보다 더 클 경우 현재 노드의 왼쪽에 있는 것으로 current_node를 왼쪽 자식 노드인 current_node.left로 갱신
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            # current_node 값이 찾고자 하는 값보다 더 작을 경우는 오른쪽 자식 노드인 current_node.riht로 갱신
            else:
                self.current_node = self.current_node.right
        return False
    
    # 노드 삭제
    def delete(self, value):
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent 됨
        is_search = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
                
        if is_search == False:
            return False
        
        # 삭제할 노드가 자식 노드를 가지고 있지 않을때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        # 삭제할 노드가 자식 노드를 가지고 있을 때(왼쪽 자식)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left 
            else:
                self.parent.right = self.current_node.left
        # 삭제할 노드가 자식 노드를 가지고 있을때(오른쪽 자식)    
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        
        #삭제할 노드가 자식 두개를 가지고 있을때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.left
            self.change_node_parent = self.current_node.right
            
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            
            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                
        return True
    
    def tree():
        

arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = Node(30)
bst = BST(root)
print()
for i in arr:
    bst.insert(i)
        
print(bst.search(22))
print(bst.search(61))
print(bst.search(60))
print(bst.delete(60))
print(bst.search(60))
print(bst.delete(22))
print(bst.delete(44))
print(bst.search(22))
print(bst.search(44))





 

