import unittest
from Source import Tess 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\projects\Numplate-Detection\Tesseract\tesseract.exe'

class TestTesseract(unittest.TestCase):

    def test_reading(self):
        self.assertEqual(Tess.Reading(1), "B23KA50")
        self.assertEqual(Tess.Reading(2), "A424A0178")
        self.assertEqual(Tess.Reading(3), "B410B0722")
        self.assertEqual(Tess.Reading(4), "C308AY799")
        self.assertEqual(Tess.Reading(5), "0474YR152")
        self.assertEqual(Tess.Reading(6), "P128YY172")
