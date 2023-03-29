import unittest


# dodać 10 rekordów i getname
from mail import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            # nie może być polskich znaków
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["julia.kowalska@student.wat.edu.pl", True, False, "Julia", "Kowalska"],
            ["adam.nowak@student.wat.edu.pl", True, True, "Adam", "Nowak"],
            ["agnieszka.mazur@wat.edu.pl", False, False, "Agnieszka", "Mazur"],
            ["piotr.kaminski@student.wat.edu.pl", True, True, "Piotr", "Kaminski"],
            ["katarzyna.adamczyk@student.wat.edu.pl", True, False, "Katarzyna", "Adamczyk"],
            ["marcin.wojciechowski@wat.edu.pl", False, True, "Marcin", "Wojciechowski"],
            ["anna.lis@student.wat.edu.pl", True, False, "Anna", "Lis"],
            ["krzysztof.pawlak@student.wat.edu.pl", True, True, "Krzysztof", "Pawlak"],
            ["ewa.nowicka@wat.edu.pl", False, False, "Ewa", "Nowicka"],
            ["jan.jakubowski@student.wat.edu.pl", True, True, "Jan", "Jakubowski"]
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname.casefold(), extractor.get_surname().casefold())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name.casefold(), extractor.get_name().casefold())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_gender())