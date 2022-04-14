class Task:
    def __init__(self, name, resources, profit):
        self.name = name
        self.resources = resources
        self.profit = profit

    def __repr__(self):
        return f'Task(name={self.name}, resources={self.resources}, profit={self.profit})'

    def __eq__(self, other):
        return (isinstance(other, self.__class__) 
            and self.name == other.name
            and self.profit == other.profit
            and self.resources == other.resources
        )