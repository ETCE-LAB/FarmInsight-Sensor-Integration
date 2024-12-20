from enum import Enum


class ListableEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
