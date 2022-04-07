class Resource:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Resource(' + self.name + ')'

    def __eq__(self, other):
        return self.name == other.name