import json
from core.selector.Resource import Resource
from core.selector.Task import Task


def as_task(dict):
    return Task(dict['name'], set(map(Resource, dict['resources'])), dict['profit'])

def _parse_json_task(json_task):
    return json.loads(json_task, object_hook = as_task)

def _parse_json_task_list(json_task_list):
    return json.loads(json_task_list, object_hook = as_task)

def parse_task_list(task_list):
    return _parse_json_task_list(task_list.replace("'", '"'))