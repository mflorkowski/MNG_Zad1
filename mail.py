import re


class EmailExtractor:

    def __init__(self, _email: str):
        self.email = _email
        self.regex = r"(?P<name>[a-z]+)[.](?P<surname>[a-z]+)[0-9]*[@](?P<student>[student]*)"
        self.test_str = self.email
        self.matches = re.search(self.regex, self.test_str)

    def is_student(self) -> bool:
        if self.matches.group(3) == "student":
            return True
        else:
            return False

    def get_name(self) -> str:
        return self.matches.group(1)

    def get_surname(self) -> str:
        return self.matches.group(2)

    def get_gender(self):
        if self.matches.group(1)[len(self.matches.group(1)) - 1] == 'a':
            return False
        else:
            return True
    