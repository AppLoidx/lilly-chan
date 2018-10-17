class Person:

    def __init__(self, person_id: str, name: str):
        self._person_id = person_id
        self._name = name
        # Прошел очередь
        self.passed = False

    def set_passed(self, passed: bool):
        self.passed = passed

    def get_id(self):
        return self._person_id

    def get_name(self):
        return self._name
