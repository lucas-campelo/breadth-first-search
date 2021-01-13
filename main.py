from sys import maxsize
from graph import Node
from algorithm import bfs

g = [
    Node(label='A' ,dist=maxsize, adj=[1, 4]),
    Node(label='B' ,dist=maxsize, adj=[2, 4]),
    Node(label='C' ,dist=maxsize, adj=[1, 3]),
    Node(label='D' ,dist=maxsize, adj=[2, 4, 5]),
    Node(label='E' ,dist=maxsize, adj=[0, 1, 3]),
    Node(label='F' ,dist=maxsize, adj=[3])
]

if __name__ == '__main__':
    tree = bfs(graph=g, start=g[0])
    for node in tree:
        print(node)