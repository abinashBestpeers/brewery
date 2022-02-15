import unittest
import requests


class TestAccountingService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5002/accounts"

    def test_records(self):
        """ Test /accounts/<name> for all known accounts"""
        for name, expected in GOOD_RESPONSES.items():
            reply = requests.get("{}/{}".format(self.url, name))
            actual_reply = reply.json()

            self.assertEqual(actual_reply, expected,
                             "Got {} but expected {}".format(
                                 actual_reply, expected
                             ))

    def test_not_found(self):
        """ Test /accounts/<name> for non-existent account"""
        invalid_account = "xyz"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_account))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
    "abinash": 54321,
    "john": 22345,
    "doe": 43434
}

if __name__ == "__main__":
    unittest.main()