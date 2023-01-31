import os
from unittest import TestCase

import cv2
from dbr import EnumBarcodeFormat

from app.decoders.dni_1997_decoder import DNI1997Decoder
from app.services.barcode_reader import DynamSoftBarcodeReader, DynamSoftBarcodeReaderOpts

current_path = os.path.dirname(os.path.abspath(__file__))

TESTDATA_PATH = os.path.join(current_path, '..', '..', 'data/1997')


class TestDNI1997Decoder(TestCase):
    decoder: DNI1997Decoder

    @classmethod
    def setUpClass(cls):
        cls.decoder = cls._get_decoder()

    def run_test_decode(self, test_number: int):
        image_path = os.path.join(TESTDATA_PATH, f'{test_number}/IMG.png')
        img_data = cv2.imread(image_path)
        expected_path = os.path.join(TESTDATA_PATH, f'{test_number}/EXPECTED.json5')
        decoded_data = TestDNI1997Decoder.decoder.decode([img_data])
        if not os.path.exists(expected_path):
            with open(expected_path, 'w') as f:
                f.write(decoded_data.json(indent=2))

        with open(expected_path, 'r') as f:
            expected_data = f.read()
            self.assertEqual(decoded_data.json(indent=2), expected_data)

    @staticmethod
    def _get_decoder():
        license_key = 'DLS2eyJoYW5kc2hha2VDb2RlIjoiMTAxMzkxMzE5LTEwMTM5MzYzMyIsIm9yZ2FuaXphdGlvbklEIjoiMTAxMzkxMzE5In0='
        opts = DynamSoftBarcodeReaderOpts(
            license_key=license_key,
            barcode_type=EnumBarcodeFormat.BF_PDF417,
            barcode_min_len=None,
        )
        reader = DynamSoftBarcodeReader(opts)
        reader.config_accuracy_first_pdf417()
        decoder = DNI1997Decoder(reader)
        return decoder

    def test_decode_1(self):
        self.run_test_decode(1)

    def test_decode_2(self):
        self.run_test_decode(2)

    def test_decode_3(self):
        self.run_test_decode(3)

    def test_decode_4(self):
        self.run_test_decode(4)

    def test_decode_5(self):
        self.run_test_decode(5)

    def test_decode_6(self):
        self.run_test_decode(6)

    def test_decode_7(self):
        self.run_test_decode(7)

    def test_decode_8(self):
        self.run_test_decode(8)

    def test_decode_9(self):
        self.run_test_decode(9)

    def test_decode_10(self):
        self.run_test_decode(10)

    def test_decode_11(self):
        self.run_test_decode(11)

    def test_decode_12(self):
        self.run_test_decode(12)

    def test_decode_13(self):
        self.run_test_decode(13)

    def test_decode_14(self):
        self.run_test_decode(14)

    def test_decode_15(self):
        self.run_test_decode(15)

    def test_decode_16(self):
        self.run_test_decode(16)

    def test_decode_17(self):
        self.run_test_decode(17)

    def test_decode_18(self):
        self.run_test_decode(18)

    def test_decode_19(self):
        self.run_test_decode(19)

    def test_decode_20(self):
        self.run_test_decode(20)

    def test_decode_21(self):
        self.run_test_decode(21)

    def test_decode_22(self):
        self.run_test_decode(22)
