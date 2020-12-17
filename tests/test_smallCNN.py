import unittest
from Source.Prediction import predicting

class Test_SmallCNN(unittest.TestCase):

    def test_true(self):
        self.assertEqual(predicting("tests/test_images/1.jpg"), 1)
        self.assertEqual(predicting("tests/test_images/2.jpg"), 1)
        self.assertEqual(predicting("tests/test_images/3.jpg"), 1)
        self.assertEqual(predicting("tests/test_images/4.jpg"), 1)
        self.assertEqual(predicting("tests/test_images/5.jpg"), 1)
        self.assertEqual(predicting("tests/test_images/6.jpg"), 1)

    def test_false(self):
        self.assertEqual(predicting("tests/test_images/1n.jpg"), 0)
        self.assertEqual(predicting("tests/test_images/2n.jpg"), 0)
        self.assertEqual(predicting("tests/test_images/3n.jpg"), 0)
        self.assertEqual(predicting("tests/test_images/4n.jpg"), 0)
        self.assertEqual(predicting("tests/test_images/5n.jpg"), 0)
        self.assertEqual(predicting("tests/test_images/6n.jpg"), 0)
