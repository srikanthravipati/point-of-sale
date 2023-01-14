import unittest

from item_basic_info import BasicInfo


class TestBasicInfo(unittest.TestCase):
    def test_constructor(self):
        basic_info = BasicInfo("Test", 2.0)
        self.assertEqual(basic_info.name, "Test")
        self.assertEqual(basic_info.price, 2.0)

    def test_set_price(self):
        basic_info = BasicInfo("Test", 2.0)
        basic_info.price = 1.0
        self.assertEqual(basic_info.price, 1.0)


if __name__ == "__main__":
    unittest.main()
