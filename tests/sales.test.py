import unittest
import requests


class TestSalesService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5001/sales"

    def test_records(self):
        """ Test /sales/<name> for all known sales"""
        for name, expected in GOOD_RESPONSES.items():
            reply = requests.get("{}/{}".format(self.url, name))
            actual_reply = reply.json()

            self.assertEqual(actual_reply, expected,
                             "Got {} but expected {}".format(
                                 actual_reply, expected
                             ))

    def test_not_found(self):
        """ Test /sales/<name> for non-existent account"""
        invalid_name = "xyz"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_name))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
    "abinash": 100,
    "john": 200,
    "doe": 300
}

if __name__ == "__main__":
    unittest.main()