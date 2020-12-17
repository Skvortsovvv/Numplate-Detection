import unittest
from Source.Yolo import detection
from Source.Prediction import predicting

class TestYolo(unittest.TestCase):

    def test_yolo(self):
        detection("images_yolo/1")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/2")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/3")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/4")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/5")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/6")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/7")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/8")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/9")
        self.assertEqual(predicting("1.jpg"), 1)
        detection("images_yolo/10")
        self.assertEqual(predicting("1.jpg"), 1)
