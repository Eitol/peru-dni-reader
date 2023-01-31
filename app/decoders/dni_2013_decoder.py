from typing import List, Optional

from app.decoders.dni_decoder import DNIDecoder, CardIdData


class DNI2013Decoder(DNIDecoder):
    def __init__(self):
        super(DNI2013Decoder, self)

    def decode(self, docs: List[bytes]) -> Optional[CardIdData]:
        raise NotImplementedError()
