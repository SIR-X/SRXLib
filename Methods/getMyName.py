from .utils import *


class getMyName:
    async def get_my_name(
        self,
        language_code : str = None,
    ):
        """
        Use this method to get the current bot name for the given user language. Returns BotName on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string.
        """

        return await Curl.request(
            url=self.api + "getMyName",
            json={
                "language_code": language_code,
            }
        )
