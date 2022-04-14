from django.test import TestCase
from core.selector.JsonParse import parse_task, parse_task_list
from core.selector.Resource import Resource
from core.selector.Task import Task


class JsonParseTest(TestCase):

    def test_parse_task(self):
        json_task = '{"name": "task1", "resources":["resource1", "resource2"], "profit":2.9}'
        task = Task('task1', {Resource('resource1'), Resource('resource2')}, 2.9)
        parsed_task = parse_task(json_task)
        self.assertEqual(parsed_task, task)

    def test_parse_empty_task_list(self):
        self.assertEqual(parse_task_list('[]'), [])
    
    def test_parse_task_list(self):
        json_task_list = '[{"name": "task1", "resources":["resource1"], "profit":2.9}, ' + \
            '{"name": "task2", "resources":["resource2"], "profit":6}]'
        task1 = Task('task1', {Resource('resource1')}, 2.9)
        task2 = Task('task2', {Resource('resource2')}, 6)
        self.assertEqual(parse_task_list(json_task_list), [task1, task2])
        