from .utils import *
import typing
from Types.InputSticker import InputSticker

class addStickerToSet:
    async def add_sticker_to_set(
        self,
        user_id : int = None,
        name : str = None,
        sticker : InputSticker = None,
    ):
        """
        Use this method to add a new sticker to a set created by the bot. The format of the added sticker must match the format of the other stickers in the set. Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

        Args:
            user_id (int): User identifier of sticker set owner.

            name (str): Sticker set name.

            sticker (InputSticker): A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed..
        """

        return await Curl.request(
            url=self.api + "addStickerToSet",
            json={
                "user_id": user_id,
                "name": name,
                "sticker": sticker,
            }
        )
