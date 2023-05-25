from .utils import *
import typing


class getCustomEmojiStickers:
    async def get_custom_emoji_stickers(
        self,
        custom_emoji_ids : list[str] = None,
    ):
        """
        Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects.

        Args:
            custom_emoji_ids (list[str]): List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified..
        """

        return await Curl.request(
            url=self.api + "getCustomEmojiStickers",
            json={
                "custom_emoji_ids": custom_emoji_ids,
            }
        )
