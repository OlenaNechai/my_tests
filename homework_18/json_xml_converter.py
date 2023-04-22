import json
from dict2xml import dict2xml
from argparse import ArgumentParser


class Human:
    def __init__(self, name: str, age: int, gender: str, birth_year: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        payload = json.dumps(self.__dict__)
        return payload

    def convert_to_xml(self):
        xml = dict2xml(self.__dict__)
        return xml


parser = ArgumentParser(description="My parser")
parser.add_argument('--format', help='Format: json or xml', default='json')
args = parser.parse_args()
user = Human('Cactus', 22, 'male', 2001)

if args.format.lower() == 'json':
    print(Human.convert_to_json(user))
elif args.format.lower() == 'xml':
    print(Human.convert_to_xml(user))
