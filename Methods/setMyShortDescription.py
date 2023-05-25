from .utils import *
import typing


class setMyShortDescription:
    async def set_my_short_description(
        self,
        short_description : str = None,
        language_code : str = None,
    ):
        """
        Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success.

        Args:
            short_description (str): New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language..

            language_code (str): A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description..
        """

        return await Curl.request(
            url=self.api + "setMyShortDescription",
            json={
                "short_description": short_description,
                "language_code": language_code,
            }
        )
