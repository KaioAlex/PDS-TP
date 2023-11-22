from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(init=True)
class Card:
    id_user: int = None
    username: str = None
    num_card: str = None
    card_validity: str = None
    security_code: int = None
    id: int = None