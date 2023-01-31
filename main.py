import os
import sys

import cv2
from dbr import EnumBarcodeFormat

from app.decoders.dni_1997_decoder import DNI1997Decoder
from app.services.barcode_reader import DynamSoftBarcodeReaderOpts, DynamSoftBarcodeReader


def run_test_decode(image_path: str):
    license_key = os.environ.get('DYNAMSOFT_LICENSE_KEY')
    if not license_key:
        raise ValueError('DYNAMSOFT_LICENSE_KEY not set')
    opts = DynamSoftBarcodeReaderOpts(
        license_key=license_key,
        barcode_type=EnumBarcodeFormat.BF_PDF417,
        barcode_min_len=None,
    )
    reader = DynamSoftBarcodeReader(opts)
    reader.config_accuracy_first_pdf417()
    decoder = DNI1997Decoder(reader)
    img_data = cv2.imread(image_path)
    decoded_data = decoder.decode([img_data])
    if decoded_data:
        print(decoded_data.json(indent=4, sort_keys=True))
    else:
        print('PDF417 not found')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py <image_path>')
        sys.exit(1)
    file_arg = sys.argv[1]
    if os.path.exists(file_arg):
        run_test_decode(file_arg)
    else:
        print('File not found: %s' % file_arg)
