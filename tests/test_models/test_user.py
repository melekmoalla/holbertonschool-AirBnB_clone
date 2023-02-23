import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_User(self):
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.password = "root"
        my_user2.save()
        self.assertEqual(my_user2, my_user2)

