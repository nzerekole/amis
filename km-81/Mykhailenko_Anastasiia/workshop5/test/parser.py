import os
from DataSet.record import Record
from xml.etree import ElementTree as ET


def get_dataset():
    path = os.path.join(os.getcwd(), 'dataset.xml')
    tree = ET.parse(path)
    return tree.getroot()


def parse_dataset(dataset=get_dataset()):
    result = []
    for element in dataset:
        obj = parse_object(element)
        result.append(Record(obj))
    return result


def parse_object(data):
    obj = {}
    for prop in data:
        key = prop.tag
        value = prop.text
        if value is not None:
            obj[key] = value
    return obj
