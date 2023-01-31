from abc import ABC, abstractmethod
from typing import Optional, Tuple

from paddleocr import paddleocr


class OCRMachine(ABC):
    @abstractmethod
    def extract_text(self, image: bytes) -> str:
        raise NotImplementedError()


#
#
# class EasyOCRMachine(OCRMachine):
#     def __init__(self):
#         # need to run only once to load model into memory
#         self._ocr = easyocr.Reader(['en'], gpu=False, )
#
#     def extract_text(self, image: bytes) -> str:
#         result: Optional[Tuple[int, int, str]] = self._ocr.readtext(image)


class PaddleOCRMachine(OCRMachine):
    def __init__(self):
        # need to run only once to load model into memory
        self._ocr = paddleocr.PaddleOCR(lang='en', use_gpu=False)

    def extract_text(self, image: bytes) -> str:
        result: Optional[Tuple[int, int, str]] = self._ocr.ocr(image)
        return result
