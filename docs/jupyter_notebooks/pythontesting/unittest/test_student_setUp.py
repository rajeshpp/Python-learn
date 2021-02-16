import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.stu1 = Student('Robin', 'Wills', 25000)
        self.stu2 = Student('Mark', 'Smith', 28000)

    def test_mail(self):
        self.assertEqual(self.stu1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(self.stu2.mail, 'Mark.Smith@xyz.com')

        self.stu1.first = "Jennifer"
        self.stu2.first = "Graham"

        self.assertEqual(self.stu1.mail, 'Jennifer.Wills@xyz.com')
        self.assertEqual(self.stu2.mail, 'Graham.Smith@xyz.com')

    def test_fullname(self):
        self.assertEqual(self.stu1.fullname, 'Robin Wills')
        self.assertEqual(self.stu2.fullname, 'Mark Smith')

        self.stu1.first = "Jennifer"
        self.stu2.first = "Graham"

        self.assertEqual(self.stu1.fullname, 'Jennifer Wills')
        self.assertEqual(self.stu2.fullname, 'Graham Smith')


    def test_stipend_hike(self):

        self.stu1.apply_hike()
        self.stu2.apply_hike()

        self.assertEqual(self.stu1.stipend, 26250)
        self.assertEqual(self.stu2.stipend, 29400)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()