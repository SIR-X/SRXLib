from .utils import *


class setMyName:
    async def set_my_name(
        self,
        name : str = None,
        language_code : str = None,
    ):
        """
        Use this method to change the bot's name. Returns True on success.

        Args:
            name (str): New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language..

            language_code (str): A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name..
        """

        return await Curl.request(
            url=api + "setMyName",
            json={
                "name": name,
                "language_code": language_code,
            }
        )
