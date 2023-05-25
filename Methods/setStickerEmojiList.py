from .utils import *


class setStickerEmojiList:
    async def set_sticker_emoji_list(
        self,
        sticker : str = None,
        emoji_list : list[str] = None,
    ):
        """
        Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker.

            emoji_list (list[str]): A JSON-serialized list of 1-20 emoji associated with the sticker.
        """

        return await Curl.request(
            url=self.api + "setStickerEmojiList",
            json={
                "sticker": sticker,
                "emoji_list": emoji_list,
            }
        )
