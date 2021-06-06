import unittest

from item_basic_info import BasicInfo


class TestBasicInfo(unittest.TestCase):
    def test_constructor(self):
        basic_info = BasicInfo("Test")
        self.assertEqual(basic_info.get_name(), "Test")
        self.assertEqual(basic_info.get_price(), 0.0)

    def test_set_price(self):
        basic_info = BasicInfo("Test")
        basic_info.set_price(1.0)
        self.assertEqual(basic_info.get_price(), 1.0)


if __name__ == "__main__":
    unittest.main()
