from .utils import *


class deleteStickerFromSet:
    async def delete_sticker_from_set(
        self,
        sticker : str = None,
    ):
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker.
        """

        return await Curl.request(
            url=api + "deleteStickerFromSet",
            json={
                "sticker": sticker,
            }
        )
