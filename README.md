# Task Selector

Given a list of tasks containing a name, a list of required resources and profit, this application outputs the list of tasks with maximum profit so that no two tasks require the same resource.

The input must be uploaded as a file with the following format:
```
[
    {'name': 'capture for client 1098', 'resources': ['camera', 'disk', 'proc'] , 'profit': 9.2},
    {'name': 'clean disk', 'resources': ['disk'] , 'profit': 0.4},
    {'name': 'upgrade to v2.1', 'resources': ['proc'] , 'profit': 2.9}
]
```

To run the application:
1. Install Docker
2. Clone the repository
3. Run `docker-compose up` in a terminal
4. Go to http://localhost:8000/selector/ and upload a file