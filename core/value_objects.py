from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zip_code: str

    def __post_init__(self):
        if not self.street or not self.city:
            raise ValueError("Via e città sono obbligatorie per un indirizzo.")

    def __str__(self):
        return f"{self.street}, {self.zip_code} {self.city}"