from orjson import dumps

class TelegramObject(dict):
    def __bytes__(self) -> bytes:
        return dumps(dict(filter(lambda x: x[1], self.items())))

    def __repr__(self) -> str:
        return self.__bytes__().decode()

    def update(self, value) -> None:
        value.pop("self")
        super().update(value)