from .utils import *
import typing


class getMyDescription:
    async def get_my_description(
        self,
        language_code : str = None,
    ):
        """
        Use this method to get the current bot description for the given user language. Returns BotDescription on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string.
        """

        return await Curl.request(
            url=self.api + "getMyDescription",
            json={
                "language_code": language_code,
            }
        )
