import unittest

class TestOrder(unittest.TestCase):
    def test_cost(self):
        img = Image(10)
        self.assertEqual(img.getCost(), 800)

        flac = Flac(15)
        self.assertEqual(flac.getCost(), 1957.50)

        vid = Video(13)
        self.assertEqual(vid.getCost(), 2370)

if __name__ == '__main__':
    unittest.main()