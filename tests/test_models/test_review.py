import unittest
from models.review import Review


class TestUser(unittest.TestCase):

    def test_User(self):
        my_user2 = Review()
        my_user2.user_id = "mayouka"
        my_user2.name = "John"
        my_user2.text = "work hard"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))