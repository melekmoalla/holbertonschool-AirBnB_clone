import unittest
from models.city import City


class TestUser(unittest.TestCase):

    def test_User(self):
        my_user2 = City()
        my_user2.state_id="242424"
        my_user2.name = "John"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))