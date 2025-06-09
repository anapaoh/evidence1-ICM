import unittest
from password_checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_strong_passwords(self):
        self.assertEqual(check_password_strength("Password123!"), "STRONG")
        self.assertEqual(check_password_strength("Admin@2023"), "STRONG")
        self.assertEqual(check_password_strength("My_Passw0rd!"), "STRONG")

    def test_weak_passwords(self):
        self.assertEqual(check_password_strength("123456"), "WEAK")
        self.assertEqual(check_password_strength("password"), "WEAK")
        self.assertEqual(check_password_strength("PASSWORD"), "WEAK")
        self.assertEqual(check_password_strength("Password"), "WEAK")
        self.assertEqual(check_password_strength("Pass123"), "WEAK")

if __name__ == '__main__':
    unittest.main()
