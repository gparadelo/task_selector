class TaskSelector:

    def resources_overlap(resources1, resources2):
        return any(resource1 in resources2 for resource1 in resources1)

    def select(tasks):
        return TaskSelector._select_recursive(tasks, [])[0]


    def _select_recursive(tasks, used_resources):
        if len(tasks) == 0:
            return (tasks, 0)

        tasksNotIncludingHead = TaskSelector._select_recursive(tasks[1:], used_resources)

        if TaskSelector.resources_overlap(used_resources, tasks[0].resources):
            return tasksNotIncludingHead

        tasksIncludingHead = TaskSelector._select_recursive(tasks[1:], used_resources + list(tasks[0].resources)) 
        tasksIncludingHead = ([tasks[0]] + tasksIncludingHead[0],
         tasks[0].profit + tasksIncludingHead[1])

        return tasksIncludingHead if tasksIncludingHead[1] > tasksNotIncludingHead[1] else tasksNotIncludingHead
        