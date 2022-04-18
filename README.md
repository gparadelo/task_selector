# Task Selector

Given a list of tasks containing a name, a list of resources it requires and profit, this application outputs the list of tasks with maximum profit so that no two tasks require the same resource.

The input must be uploaded as a file with the following format:
```
[
    {'name': 'capture for client 1098', 'resources': ['camera', 'disk', 'proc'] , 'profit': 9.2},
    {'name': 'clean disk', 'resources': ['disk'] , 'profit': 0.4},
    {'name': 'upgrade to v2.1', 'resources': ['proc'] , 'profit': 2.9}
]
```

### To run the application:
1. Install Docker
2. Clone the repository
3. Run `docker-compose up` in a terminal
4. Go to http://localhost:8000/selector/, upload a file and click 'Save'

### Further Work:
1. Improve error messages: describe the problem with the input (bad format, missing key, wrong type of value, etc.).
2. Improve UX.
3. Optimize selection algorithm:
    - When modelling the problem as a graph with tasks as nodes and nodes are connected when a resource is shared, precompute disjoint sets and solve the problem separately for each set. 
    - The current algorithm extends all possible solutions completely. This is highly inefficient since many solutions can be discarded at earlier stages. To achieve this we must take advantage of the fact that if two partial solutions have considered the same tasks and consume the same resources, only the one with highest profit needs to be extended further, the other will always yield a worse (or equal) final solution. 
    The steps to implement this are: 
        - Make the algorithm iterative. 
        - Store each iteration's subproblem in matrix or hash table indexed by [n],[resources consumed] where n is the index of the last task considered. 
        - When extending a subproblem with a new task, compare the resulting subproblem with previous ones encountered that consumed the same resources and considered the same tasks. If one exists with higher profit, the subproblem can be discarded and not extended any further to save time.