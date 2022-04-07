import resource


class TaskSelector:

    def resourcesOverlap(resources1, resources2):
        return any(resource1 in resources2 for resource1 in resources1)

    def select(tasks):
        return TaskSelector._selectRecursive(tasks, [])[0]


    def _selectRecursive(tasks, usedResources):
        if len(tasks) == 0:
            return (tasks, 0)

        tasksNotIncludingHead = TaskSelector._selectRecursive(tasks[1:], usedResources)

        if TaskSelector.resourcesOverlap(usedResources, tasks[0].resources):
            return tasksNotIncludingHead

        tasksIncludingHead = TaskSelector._selectRecursive(tasks[1:], usedResources + tasks[0].resources) 
        tasksIncludingHead = ([tasks[0]] + tasksIncludingHead[0],
         tasks[0].profit + tasksIncludingHead[1])

        return tasksIncludingHead if tasksIncludingHead[1] > tasksNotIncludingHead[1] else tasksNotIncludingHead
        