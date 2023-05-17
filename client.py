from Methods import Methods
from Types   import *

from fastapi import FastAPI, Request
from orjson  import loads

class Bot(FastAPI, Methods):
    def __init__(self, bot_token: str):
        Methods.__init__(self)
        FastAPI.__init__(self)

        self.api = f"https://api.telegram.org/bot{bot_token}/"

    def on_update(self, webhook: str = "/webhook"):
        def decorator(func):
            @self.post(webhook)
            async def wrapper(request: Request):
                update = loads(await request.body())
                return await func(self, update)
            return wrapper
        return decorator

    def on_message(self):
        def decorator(func):
            @self.on_update()
            async def wrapper(self, update: dict):
                if "message" in update:
                    return await func(self, update["message"])
            return wrapper
        return decorator