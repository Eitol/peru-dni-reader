import os

import cv2
from dbr import EnumBarcodeFormat

from app.decoders.peru.dni_1997_decoder import DNI1997Decoder
from app.services.barcode_reader import DynamSoftBarcodeReaderOpts, DynamSoftBarcodeReader


def rename_pdf_files(directory):
    license_key = '' # Add licence key here
    opts = DynamSoftBarcodeReaderOpts(
        license_key=license_key,
        barcode_type=EnumBarcodeFormat.BF_PDF417,
        barcode_min_len=None,
    )
    reader = DynamSoftBarcodeReader(opts)
    reader.config_accuracy_first_pdf417()
    decoder = DNI1997Decoder(reader)
    # Recorrer los directorios y archivos de forma recursiva
    for root, dirs, files in os.walk(directory):
        # Recorrer la lista de archivos
        for file in files:
            new_name = ''
            # Obtener el path completo del archivo
            file_path = os.path.join(root, file)
            # Comprobar si el archivo es un PDF
            if file.endswith("PDF417.png"):
                image_path = file_path
                raw_content_path = file_path.replace('PDF417.png', 'PDF417.txt')
                img_data = cv2.imread(image_path)
                try:
                    raw_data = reader.read(img_data)
                    with open(raw_content_path, 'wb') as f:
                        f.write(raw_data)
                        print('File created: {}'.format(raw_content_path))
                except Exception as e:
                    print(f'the file {file_path} could not be read')
                    continue


if __name__ == '__main__':
    # Ejemplo de uso del código
    rename_pdf_files("peru-dni-reader/test/data/1997")
