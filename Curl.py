import pycurl
import asyncio
from io import BytesIO
from typing import Literal
from orjson import loads, dumps
from urllib.parse import urlencode

def get_headers(headers: dict) -> list:
    return [
        f"{key}:{value}"
        for key, value in headers.items()
    ]

def remove_none_values(input_data):
    if isinstance(input_data, dict):
        for key, value in dict(input_data).items():
            if value is None:
                del input_data[key]

            elif isinstance(value, (dict, list)):
                remove_none_values(value)

    elif isinstance(input_data, list):
        for value in input_data:
            if value is None:
                input_data.remove(value)

            elif isinstance(value, (dict, list)):
                remove_none_values(value)

    return input_data


async def get(url: str, headers: dict = {}):
    curl = pycurl.Curl()

    with BytesIO() as buffer:
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.setopt(pycurl.HTTPHEADER, get_headers(headers))

        await asyncio.get_running_loop().run_in_executor(None, curl.perform)
        curl.close()

        return buffer.getvalue()

async def post(url: str, data: dict = {}, json: dict = {}, headers: dict = {}, files: str = []):
    curl = pycurl.Curl()

    json = remove_none_values(json)
    data = remove_none_values(data)

    with BytesIO() as buffer:
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.HTTPHEADER, get_headers(headers))


        if files:
            curl.setopt(curl.HTTPPOST, [
                        ("upload_file", (curl.FORM_FILE, file)) for file in files])

        elif json:
            curl.setopt(curl.HTTPHEADER, ["Content-Type: application/json"])
            curl.setopt(pycurl.POSTFIELDS, dumps(json))

        elif data:
            curl.setopt(pycurl.POSTFIELDS, urlencode(data))

        await asyncio.get_running_loop().run_in_executor(None, curl.perform)
        curl.close()

        return buffer.getvalue()


async def request(method: Literal["post", "get"] = "post", *args, **kwargs):
    match method:
        case "post":
            return loads(await post(*args, **kwargs))

        case "get":
            return loads(await get(*args, **kwargs))

    raise ValueError(f"There is no method named \"{method}\"")