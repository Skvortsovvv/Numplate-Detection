import unittest
from Source.Yolo import detection
from Source.Prediction import predicting

class TestYolo(unittest.TestCase):

    def test_yolo(self):
        detection("tests/test_yolo_images/1")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/2")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/3")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/4")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/5")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/6")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/7")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/8")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/9")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("tests/test_yolo_images/10")
        self.assertEqual(predicting("1.jpg"), 1)
