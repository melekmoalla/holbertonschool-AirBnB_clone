import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state(self):
        my_user2 = State()
        my_user2.name = "John"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))

    