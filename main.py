from Methods import Methods
from Types   import *

from fastapi import FastAPI, Request
from orjson  import loads

class Bot(FastAPI, Methods):
    def __init__(self):
        Methods.__init__(self)
        FastAPI.__init__(self)

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

    def on_callback_query(self):
        def decorator(func):
            @self.on_update()
            async def wrapper(self, update: dict):
                if "callback_query" in update:
                    return await func(self, update["callback_query"])
            return wrapper
        return decorator

app = Bot()

@app.on_message()
async def OnMessage(client: Bot, update: dict):
    await client.send_message(1844840402, text="OnMessage Called !")
    await client.send_message(1844840402, text=f"OnMessage Update: {update}")


# @app.post("/webhook")
# async def on_update(request: Request):
#     update = await json_to_dict(request)

#     print(
#         await app.send_message(update["message"]["from"]["id"], text="hihi")
#     )