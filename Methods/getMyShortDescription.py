from .utils import *


class getMyShortDescription:
    async def get_my_short_description(
        self,
        language_code : str = None,
    ):
        """
        Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string.
        """

        return await Curl.request(
            url=self.api + "getMyShortDescription",
            json={
                "language_code": language_code,
            }
        )
