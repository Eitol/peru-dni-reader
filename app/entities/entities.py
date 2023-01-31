from enum import Enum
from typing import Optional

from pydantic import BaseModel


class DocumentType(str, Enum):
    DNI_1997_ADULT = "dni_1997_adult"
    DNI_1997_MINOR = "dni_1997_minor"
    DNI_E_2013 = "dni_e_2013"
    DNI_E_2020 = "dni_e_2020"


class Location(BaseModel):
    department: str
    department_code: str
    municipality: str
    municipality_code: str


class DocumentInfo(BaseModel):
    document_number: str
    expiration_date: str
    token_code: str
    document_type: DocumentType


class CardIdData(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    second_last_name: str
    birth_date: Optional[str]
    gender: str
    location: Optional[Location]
    document_info: DocumentInfo
