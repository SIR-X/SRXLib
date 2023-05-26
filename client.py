from Methods import Methods
from Types   import *

from fastapi import FastAPI, Request
from orjson  import loads

from types import FunctionType
from asyncio import gather




class Bot(FastAPI, Methods):
    def __init__(
        self,
        bot_token: str,
        webhook_url: str = None
    ):
        Methods.__init__(self)
        FastAPI.__init__(self)

        self.api = f"https://api.telegram.org/bot{bot_token}/"
        self.webhook_url = webhook_url

        self.handlers = dict.fromkeys(Update.__init__.__code__.co_varnames[2:], [])

        self.add_event_handler("startup", self.startup_event)
        self.router.add_api_route("/webhook", self.handle_update, methods=["POST"])

    async def startup_event(self):
        if self.webhook_url:
            await self.delete_webhook()
            await self.set_webhook(
                self.webhook_url,
                allowed_updates=list(self.handlers)
            )

    async def handle_update(self, request: Request):
        update : dict = loads(await request.body())
        update.pop("update_id")

        for key, value in update.items():
            await gather(func(self, value) for func in self.handlers[key])

    def add_handler(self, handler: str, function: FunctionType):
        if handler in self.handlers:
            if function not in self.handlers[handler]:
                self.handlers[handler].append(function)

        else:
            raise ValueError(f"Invalid handler: {handler}")
