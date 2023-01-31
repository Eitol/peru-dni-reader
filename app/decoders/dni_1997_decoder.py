from typing import List, Optional

from app.decoders.dni_decoder import DNIDecoder
from app.entities.entities import CardIdData, DocumentInfo, DocumentType
from app.services.barcode_reader import AbstractBarcodeReader

PDF417_ENCODING = 'latin-1'

class DNI1997Decoder(DNIDecoder):
    def __init__(self, barcode_reader: AbstractBarcodeReader):
        super(DNI1997Decoder, self)
        self.barcode_reader = barcode_reader

    def decode(self, docs: List[bytes]) -> Optional[CardIdData]:
        for doc in docs:
            result = self.barcode_reader.read(doc)
            if not result:
                continue
            data, barcode_type = result
            if barcode_type == 'PDF417':
                card_id_data = self._decode_pdf417(data)
                if card_id_data:
                    return card_id_data
        return None

    @staticmethod
    def _decode_pdf417(data: bytes) -> Optional[CardIdData]:
        """
        Bytes	Campo	                            Ejemplo
        2-9	    Número de documento	                45595338
        10-49	Primer Apellido	                    Castillo
        50-89	Segundo apellido	                Ceferino
        90-124	Nombres (separados por un espacio)	Norman Valery
        125	    Sexo	1: Masculino, 2: Femenino   1
        448-455	Fecha de vencimiento en formato yyyy/MM/DD	        20270425 (equivalente a 25/04/2027 o 25 de Abril del 2027)
        456-463	Código de ficha 	                87260138
        :param data:
        :return:
        """
        if len(data) < 470:
            return None
        doc_number = data[2:10].decode(PDF417_ENCODING).strip()
        last_name = data[10:50].decode(PDF417_ENCODING).strip()
        second_last_name = data[50:90].decode(PDF417_ENCODING).strip()
        names = data[90:125].decode(PDF417_ENCODING).strip()
        first_name, middle_name = DNI1997Decoder._decode_names_from_pdf417(names)
        gender = DNI1997Decoder._decode_gender_from_pdf417(data)
        expiration_date_raw = data[448:456].decode(PDF417_ENCODING).strip()
        # in fmt dd/mm/yyyy
        expiration_date = f'{expiration_date_raw[6:8]}/{expiration_date_raw[4:6]}/{expiration_date_raw[0:4]}'
        token_code = data[456:464].decode(PDF417_ENCODING).strip()
        return CardIdData(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            second_last_name=second_last_name,
            gender=gender,
            document_info=DocumentInfo(
                document_number=doc_number,
                expiration_date=expiration_date,
                token_code=token_code,
                document_type=DocumentType.DNI_1997_ADULT
            )
        )

    @staticmethod
    def _decode_gender_from_pdf417(data):
        gender_code = data[125:126].decode(PDF417_ENCODING).strip()
        if gender_code == '1':
            gender = 'M'
        elif gender_code == '2':
            gender = 'F'
        else:
            gender = 'O'
        return gender

    @staticmethod
    def _decode_names_from_pdf417(names):
        first_name, middle_name = '', ''
        if ' ' in names:
            sp = names.split(' ', 1)
            if len(sp) == 1:
                first_name, middle_name = sp
            else:
                first_name = sp[0]
                middle_name = ' '.join(sp[1:])
        return first_name, middle_name
