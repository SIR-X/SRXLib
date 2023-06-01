from Handlers import BaseHandler, DHandlers
from Methods  import Methods
from Types    import Update

from fastapi import FastAPI, Request
from orjson  import loads
from asyncio import gather


class Bot(FastAPI, Methods, DHandlers):
    def __init__(
        self,
        bot_token: str,
        webhook_url: str = None,
        api : str = None
    ) -> None:
        Methods.__init__(self)
        FastAPI.__init__(self)
        DHandlers.__init__(self)

        self.api = (api or "https://api.telegram.org/bot{0}/").format(bot_token)
        self.webhook_url = webhook_url

        self.handlers = {update_type: set() for update_type in Update.__init__.__code__.co_varnames[2:]}

        self.add_event_handler("startup", self.startup_event)
        self.router.add_api_route("/webhook", self.handle_update, methods=["POST"])

    async def startup_event(self) -> None:
        if self.webhook_url:
            await self.delete_webhook()
            await self.set_webhook(
                self.webhook_url,
                allowed_updates=list(self.handlers)
            )

    async def handle_update(self, request: Request) -> None:
        update : dict = loads(await request.body())
        update.pop("update_id")

        for key, value in update.items():
            await gather(
                *(
                    func.func(self, value)
                    for func in self.handlers[key]
                    if func.filters(self, value)
                )
            )

    def add_handler(self, handler: BaseHandler):
        self.handlers[handler.name].add(handler)
        return handler
