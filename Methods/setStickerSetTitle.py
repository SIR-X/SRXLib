from .utils import *


class setStickerSetTitle:
    async def set_sticker_set_title(
        self,
        name : str = None,
        title : str = None,
    ):
        """
        Use this method to set the title of a created sticker set. Returns True on success.

        Args:
            name (str): Sticker set name.

            title (str): Sticker set title, 1-64 characters.
        """

        return await Curl.request(
            url=self.api + "setStickerSetTitle",
            json={
                "name": name,
                "title": title,
            }
        )
