import unittest
from password_checker import is_strong

class TestPasswordStrength(unittest.TestCase):

    def test_strong_passwords(self):
        self.assertTrue(is_strong("Password123!"))
        self.assertTrue(is_strong("Admin@2023"))
        self.assertTrue(is_strong("MyPassw0rd!"))

    def test_weak_passwords(self):
        self.assertFalse(is_strong("123456"))
        self.assertFalse(is_strong("password"))
        self.assertFalse(is_strong("PASSWORD"))
        self.assertFalse(is_strong("Password"))
        self.assertFalse(is_strong("Pass123"))

if __name__ == '__main__':
    unittest.main()
