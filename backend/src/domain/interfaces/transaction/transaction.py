from dataclasses import dataclass
import datetime
from dataclasses_json import dataclass_json, LetterCase

# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(init=True)
class Transaction:
    id_src: int
    id_dest: int
    value: float
    date: datetime
    flag: int