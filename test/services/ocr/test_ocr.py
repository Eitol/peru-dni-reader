import os
from unittest import TestCase

from app.services.ocr import PaddleOCRMachine

current_path = os.path.dirname(os.path.abspath(__file__))


class TestOCRMachine(TestCase):
    def test_extract_text(self):
        machine = PaddleOCRMachine()
        image_path = os.path.join(current_path, '..', '..', 'data', '1997', '1', 'IMG.png')
        with open(image_path, 'rb') as f:
            result = machine.extract_text(f.read())
            result = machine.extract_text(f.read())
            self.assertEqual(len(result), 1)
