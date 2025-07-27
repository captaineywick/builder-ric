from dataclasses import dataclass


@dataclass
class File:
    name: str
    content: str = ""  # Optional: empty string for now
