from .utils import *
import typing


class setStickerPositionInSet:
    async def set_sticker_position_in_set(
        self,
        sticker : str = None,
        position : int = None,
    ):
        """
        Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker.

            position (int): New sticker position in the set, zero-based.
        """

        return await Curl.request(
            url=self.api + "setStickerPositionInSet",
            json={
                "sticker": sticker,
                "position": position,
            }
        )
