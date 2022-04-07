class Task:
    def __init__(self, name, resources, profit):
        self.name = name
        self.resources = resources
        self.profit = profit

    def __repr__(self):
        return f'Task({self.name}, {self.resources}, {self.profit})'