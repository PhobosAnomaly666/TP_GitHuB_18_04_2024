import unittest

from Password_Generator import generatePassword

class TestGeneratePassword(unittest.TestCase):

    def test_generatePassword(self):
        # Test avec une longueur de mot de passe de 5
        passwords = generatePassword([8, 10])
        self.assertEqual(len(passwords), 2)  # Vérifier qu'un mot de passe a été généré
        for password in passwords:
            self.assertEqual(len(password), 8)

if __name__ == '__main__':
    unittest.main()