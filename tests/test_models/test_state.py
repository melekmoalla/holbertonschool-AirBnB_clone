import unittest
from models.state import State


class TestUser(unittest.TestCase):

    def test_User(self):
        my_user2 = State()
        my_user2.name = "John"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))
