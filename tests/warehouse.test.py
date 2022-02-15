import unittest
import requests


class TestWarehouseService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5003/warehouse/beer"

    def test_records(self):
        """ Test /warehouse/beer/<name> for all known beers"""
        for name, expected in GOOD_RESPONSES.items():
            reply = requests.get("{}/{}".format(self.url, name))
            actual_reply = reply.json()

            self.assertEqual(actual_reply, expected,
                             "Got {} beer but expected {}".format(
                                 actual_reply, expected
                             ))

    def test_not_found(self):
        """ Test /warehouse/beer/<name> for non-existent beer"""
        invalid_beer = "john"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_beer))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
    "carlsberg": 5,
    "kingfisher": 2,
    "foster": 4
}

if __name__ == "__main__":
    unittest.main()