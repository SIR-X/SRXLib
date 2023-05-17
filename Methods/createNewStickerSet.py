from .utils import *
from Types.InputSticker import InputSticker

class createNewStickerSet:
    async def create_new_sticker_set(
        self,
        user_id : int = None,
        name : str = None,
        title : str = None,
        stickers : list[InputSticker] = None,
        sticker_format : str = None,
        sticker_type : str = None,
        needs_repainting : bool = None,
    ):
        """
        Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success.

        Args:
            user_id (int): User identifier of created sticker set owner.

            name (str): Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters..

            title (str): Sticker set title, 1-64 characters.

            stickers (list[InputSticker]): A JSON-serialized list of 1-50 initial stickers to be added to the sticker set.

            sticker_format (str): Format of stickers in the set, must be one of “static”, “animated”, “video”.

            sticker_type (str): Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created..

            needs_repainting (bool): Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only.
        """

        return await Curl.request(
            url=api + "createNewStickerSet",
            json={
                "user_id": user_id,
                "name": name,
                "title": title,
                "stickers": stickers,
                "sticker_format": sticker_format,
                "sticker_type": sticker_type,
                "needs_repainting": needs_repainting,
            }
        )
