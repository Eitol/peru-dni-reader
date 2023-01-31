from abc import ABC, abstractmethod
from typing import Optional, List

from app.entities.entities import CardIdData


class DNIDecoder(ABC):

    @abstractmethod
    def decode(self, docs: List[bytes]) -> Optional[CardIdData]:
        raise NotImplementedError()
