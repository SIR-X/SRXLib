from .utils import *
import typing


class setCustomEmojiStickerSetThumbnail:
    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        name : str = None,
        custom_emoji_id : str = None,
    ):
        """
        Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success.

        Args:
            name (str): Sticker set name.

            custom_emoji_id (str): Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail..
        """

        return await Curl.request(
            url=self.api + "setCustomEmojiStickerSetThumbnail",
            json={
                "name": name,
                "custom_emoji_id": custom_emoji_id,
            }
        )
