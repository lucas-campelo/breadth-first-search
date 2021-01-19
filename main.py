from sys import maxsize, path
path.append('./modules')

from modules.graph import Node
from modules.algorithm import bfs

g = [
    Node(label='A' ,dist=maxsize, adj=[1, 3]),
    Node(label='B' ,dist=maxsize, adj=[0, 2, 5]),
    Node(label='C' ,dist=maxsize, adj=[1, 6]),
    Node(label='D' ,dist=maxsize, adj=[0, 5, 4]),
    Node(label='E' ,dist=maxsize, adj=[3, 5, 6]),
    Node(label='F' ,dist=maxsize, adj=[1, 3, 4]),
    Node(label='G' ,dist=maxsize, adj=[2, 1, 4, 7]),
    Node(label='H' ,dist=maxsize, adj=[6])
]

if __name__ == '__main__':
    tree = bfs(graph=g, start=g[0])
    for node in tree:
        print(node)