from modules import Node
from queue import Queue
from typing import List

def bfs(graph: List[Node], start: Node):
    start.color = 'g'
    start.dist = 0
    start.parent = start
    q = Queue(maxsize=len(graph))
    q.put(start)

    while not q.empty():
        current = q.get()
        for n in current.adj:
            if graph[n].color == 'w':
                graph[n].color = 'g'
                graph[n].dist = current.dist + 1
                graph[n].parent = current
                q.put(graph[n])
        current.color = 'b'
    return graph