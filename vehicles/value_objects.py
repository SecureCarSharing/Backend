import re
from dataclasses import dataclass

# Lettere ammesse: A-Z tranne I, O, Q, U
_LETTERE = "A-HJ-NPR-TV-Z"
_PATTERN = re.compile(rf"[{_LETTERE}]{{2}}\d{{3}}[{_LETTERE}]{{2}}")
@dataclass(frozen=True)
class Plate:
    number: str

    def __post_init__(self):
        normalized = re.sub(r"[\s-]", "", self.number or "").upper()
        if not _PATTERN.fullmatch(normalized):
            raise ValueError(
                f"Targa non valida: {self.number!r} (formato atteso: AA 000 AA)."
            )
        object.__setattr__(self, "number", normalized)

    def __str__(self):
        return f"{self.number[:2]} {self.number[2:5]} {self.number[5:]}"


_BRAND_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9]+(?:(?: |-| & )[A-Za-z0-9]+)*")
@dataclass(frozen=True)
class Brand:
    name: str

    def __post_init__(self):
        if not isinstance(self.name, str) or len(self.name) > 30:
            raise ValueError("La marca deve essere un testo di massimo 30 caratteri.")
        normalized = " ".join(self.name.split())
        if not _BRAND_PATTERN.fullmatch(normalized):
            raise ValueError("Marca non valida.")
        object.__setattr__(self, "name", normalized.upper())

    def __str__(self):
        return self.name


_MODEL_PATTERN = re.compile(r"[A-Za-z0-9]+(?:[ -][A-Za-z0-9]+)*")
@dataclass(frozen=True)
class ModelName:
    name: str

    def __post_init__(self):
        if not isinstance(self.name, str) or not 1 <= len(self.name) <= 50:
            raise ValueError("Il modello deve avere tra 1 e 50 caratteri.")
        normalized = " ".join(self.name.split())
        if not _MODEL_PATTERN.fullmatch(normalized):
            raise ValueError(f"Modello non valido: {self.name!r}")
        object.__setattr__(self, "name", normalized)

    def __str__(self):
        return self.name