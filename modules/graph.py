from typing import List

class Node:
    def __init__(self, label: str, dist: int, adj: List[int]):
        self.label = label
        self.dist = dist
        self.adj = adj
        self.parent = None
        self.color = 'w'

    def __repr__(self):
        return f"<Label: {self.label}, Color: {self.color} Parent: {self.parent.label}, Distance: {self.dist}>"