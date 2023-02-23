import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):

    def test_User(self):
        my_user2 = Amenity()
        my_user2.name="mayouka_evnets"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))
