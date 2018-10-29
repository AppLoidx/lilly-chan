class Person:

    def __init__(self, person_id: str, name: str):
        self._person_id = person_id
        self._name = name
        # Прошел очередь
        self._passed = False

    def set_passed(self, passed: bool):
        self._passed = passed

    def get_id(self) -> str:
        return self._person_id

    def get_name(self) -> str:
        return self._name

    def get_passed(self):
        return self._passed