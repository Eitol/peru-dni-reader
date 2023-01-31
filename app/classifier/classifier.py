from abc import ABC, abstractmethod
from typing import Optional, List

from app.entities.entities import DocumentType


class DNIClassifier(ABC):

    @abstractmethod
    def classify(self, docs: List[bytes]) -> Optional[DocumentType]:
        pass


class SimpleDNIClassifier(DNIClassifier):

    def classify(self, docs: List[bytes]) -> Optional[DocumentType]:
        pass
