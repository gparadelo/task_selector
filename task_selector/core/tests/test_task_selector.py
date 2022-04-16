from django.test import TestCase
from core.selector.TaskSelector import TaskSelector
from core.selector.Resource import Resource
from core.selector.Task import Task

class TaskSelectorTest(TestCase):

    def test_select_empty_list(self):
        self.assertEqual(TaskSelector.select([]), [])

    def test_select_non_overlapping_list(self):
        task1 = Task('task1', [Resource('resource1')], 10)
        task2 = Task('task2', [Resource('resource2')], 10)
        self.assertEqual(TaskSelector.select([task1, task2]), [task1, task2])
        
    def test_resource_overpal(self):
        self.assertTrue(TaskSelector.resources_overlap([Resource('resource1')], [Resource('resource1')]))
        self.assertFalse(TaskSelector.resources_overlap([Resource('resource1')], [Resource('resource2')]))

    def test_select_overlapping_tasks(self):
        task1 = Task('task1', [Resource('resource1')], 12)
        task2 = Task('task2', [Resource('resource1')], 10)
        self.assertEqual(TaskSelector.select([task1, task2]), [task1])

    def test_select_non_greedy_solution(self):
        task1 = Task('task1', [Resource('resource1'), Resource('resource2')], 12)
        task2 = Task('task2', [Resource('resource1')], 10)
        task3 = Task('task3', [Resource('resource2')], 10)
        self.assertEqual(TaskSelector.select([task1, task2, task3]), [task2, task3])