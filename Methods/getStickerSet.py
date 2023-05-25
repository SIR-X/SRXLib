from .utils import *


class getStickerSet:
    async def get_sticker_set(
        self,
        name : str = None,
    ):
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.

        Args:
            name (str): Name of the sticker set.
        """

        return await Curl.request(
            url=self.api + "getStickerSet",
            json={
                "name": name,
            }
        )
