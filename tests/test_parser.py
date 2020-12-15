import unittest
from Source.ParseNumplate import NumPlateParser

class TestParser(unittest.TestCase):

    def test_wrong_format(self):
        self.assertEqual(NumPlateParser("abc"), "")
        self.assertEqual(NumPlateParser("o8888o7777"), "")
        self.assertEqual(NumPlateParser(""), "")

    def test_rigth_format(self):
        self.assertEqual(NumPlateParser("o887oo98"), "O887OO98")
        self.assertEqual(NumPlateParser("e777Kx777"), "E777KX777")
        self.assertEqual(NumPlateParser("B001аH01"), "B001АH01")

    def test_errors(self):
        self.assertEqual(NumPlateParser("0887oo98"), "Sorry, but character " + '"' + "0" + '"' + " cant be here")
        self.assertEqual(NumPlateParser("bX01ha01"), "Sorry, but character " + '"' + "X" + '"' + " cant be here")
        self.assertEqual(NumPlateParser("H001hoZ8"), "Sorry, but character " + '"' + "Z" + '"' + " cant be here")
        self.assertEqual(NumPlateParser("e777Kх666"), "Sorry, but there is no such region")
        self.assertEqual(NumPlateParser("o000oo01"), "Sorry, but numbers cant be 000")

if __name__ == "__main__":
    unittest.main()
