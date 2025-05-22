from password_checker import is_strong

def test_password_strength():
    assert is_strong("Password123!") == True
    assert is_strong("hello123") == False
    assert is_strong("ABCDabcd!") == False
    assert is_strong("P@ssw0rd") == True
    assert is_strong("abc") == False
    assert is_strong("SuperSecure@1") == True
    assert is_strong("123456") == False
    assert is_strong("Qwerty@789") == True
    assert is_strong("Zxcvb!123") == True
    print("All tests passed.")

if __name__ == "__main__":
    test_password_strength()
