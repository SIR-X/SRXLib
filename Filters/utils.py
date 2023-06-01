from client import Bot


class BaseFilter:
    def __call__(self, client: Bot, update: dict) -> bool:
        return NotImplemented

    def __invert__(self):
        return Invert(self)

    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

class Invert(BaseFilter):
    def __init__(self, base_filter) -> None:
        self.base_filter = base_filter

    def __call__(self, client: Bot, update: dict) -> bool:
        return not self.base_filter(update)

class Or(BaseFilter):
    def __init__(self, base_filter, other_filter) -> None:
        self.base_filter  = base_filter
        self.other_filter = other_filter

    def __call__(self, client: Bot, update: dict) -> bool:
        return self.base_filter(update) or self.other_filter(update)

class And(BaseFilter):
    def __init__(self, base_filter, other_filter) -> None:
        self.base_filter  = base_filter
        self.other_filter = other_filter

    def __call__(self, client: Bot, update: dict) -> bool:
        return self.base_filter(update) and self.other_filter(update)

def make_filter(func, name: str = "TheFilter", **kwargs) -> BaseFilter:
    return type(name, (BaseFilter,), {"__call__": func} | kwargs)()
