# Breadth First Search
<div style="text-align: justify;">
Breadth Firs Search (BFS for short) is a traversing algorithm which objective is to find connected components or trees of a graph. This repository means to present my implementation of the algorithm for Graph Theory class. I'll also try to explain the algorithm step by step. Let's get started.
</div>
<br>
<div style="text-align: justify;">
The idea behind BFS is to, starting from a arbitrarily choosen node, visit all its neighbours before going deeper in level. So for example, if I choose a vertex A, which is adjacent to B, C and D, I'd visit B, C and D before visiting their neighbours. "Well, how do I know if some vertex is visited?" We'll colour them white (if it wasn't visited), grey (if it was visited, but not all of its neighbour were visited) or black (if it was visited and all of its neighbours as well).
</div>
<br>
<div style="text-align: justify;">
Nodes in a graph must be represented by a label, a color and its neighbours. We'll also add two properties for the nodes: its distance in edges to the root (the arbitrarily choosen starting node for the algorithm) and its parent (since we're going to return a tree by the end of the algorithm). They'll look like this:
</div>
<br>

    class Node:
    def __init__(self, label: str, dist: int, adj: List[int]):
        self.label = label
        self.dist = dist
        self.adj = adj
        self.parent = None
        self.color = 'w'

## Execution
<div style="text-align: justify;">
The execution walks in the following steps:
<ol>
<li>Start all nodes with white color and infinite distance, and choose one to start with grey color and distance of zero. This is our root;</li>
<li>Create a queue and put root in there (I use Python's embed <a href="https://docs.python.org/3/library/queue.html">queue module</a>);</li>
<li>Visit all of root's neighbours:
<ul>
<li>If neighbour is white, colour it grey, set root as its parent, set its distance equal to its parent's distance plus 1 and add it to the queue;</li>
<li>If neighbour is not white, go to the next one;</li>
</ul>
</li>
<li>Remove root from queue and repeat the process until queue is empty;</li>
</ol>
</div>

<div style="text-align: justify;">
Here's an old school gif to help you understand:
</div>
<br>

<div style="text-align: center;">
<img src="https://s2.gifyu.com/images/8bit-bfs.gif">
</div>
<br>

<div style="text-align: justify;">
Hope this helps you!
</div>
