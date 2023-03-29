class EmailExtractor:

    def __init__(self, _email: str):
        self.email = _email

    def is_student(self) -> bool:
        return False

    def get_name(self) -> str:
        return "Norbert"

    def get_surname(self) -> str:
        return "Waszkowiak"
    