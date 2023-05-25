from .utils import *
import typing


class setStickerKeywords:
    async def set_sticker_keywords(
        self,
        sticker : str = None,
        keywords : list[str] = None,
    ):
        """
        Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker.

            keywords (list[str]): A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters.
        """

        return await Curl.request(
            url=self.api + "setStickerKeywords",
            json={
                "sticker": sticker,
                "keywords": keywords,
            }
        )
