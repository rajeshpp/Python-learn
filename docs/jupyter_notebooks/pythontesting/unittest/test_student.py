import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_mail(self):
        stu1 = Student('Robin', 'Wills', 25000)
        stu2 = Student('Mark', 'Smith', 25000)

        self.assertEqual(stu1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(stu2.mail, 'Mark.Smith@xyz.com')

        stu1.first = "Jennifer"
        stu2.first = "Graham"

        self.assertEqual(stu1.mail, 'Jennifer.Wills@xyz.com')
        self.assertEqual(stu2.mail, 'Graham.Smith@xyz.com')

    def test_fullname(self):
        stu1 = Student('Robin', 'Wills', 25000)
        stu2 = Student('Mark', 'Smith', 25000)

        self.assertEqual(stu1.fullname, 'Robin Wills')
        self.assertEqual(stu2.fullname, 'Mark Smith')

        stu1.first = "Jennifer"
        stu2.first = "Graham"

        self.assertEqual(stu1.fullname, 'Jennifer Wills')
        self.assertEqual(stu2.fullname, 'Graham Smith')


    def test_stipend_hike(self):
        stu1 = Student('Robin', 'Wills', 25000)
        stu2 = Student('Mark', 'Smith', 28000)

        stu1.apply_hike()
        stu2.apply_hike()

        self.assertEqual(stu1.stipend, 26250)
        self.assertEqual(stu2.stipend, 29400)

if __name__ == '__main__':
    unittest.main()