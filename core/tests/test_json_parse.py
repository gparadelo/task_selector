from django.test import TestCase
from core.selector.JsonParse import parse_task
from core.selector.Resource import Resource
from core.selector.Task import Task


class JsonParseTest(TestCase):

    def test_parse_task(self):
        jsonTask = '{"name": "task1", "resources":["resource1"], "profit":2.9}'
        task = Task('task1', {Resource('resource1')}, 2.9)
        self.assertEqual(parse_task(jsonTask), task)