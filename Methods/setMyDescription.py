from .utils import *


class setMyDescription:
    async def set_my_description(
        self,
        description : str = None,
        language_code : str = None,
    ):
        """
        Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success.

        Args:
            description (str): New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language..

            language_code (str): A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description..
        """

        return await Curl.request(
            url=api + "setMyDescription",
            json={
                "description": description,
                "language_code": language_code,
            }
        )
