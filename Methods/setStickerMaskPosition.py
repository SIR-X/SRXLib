from .utils import *
import typing
from Types.MaskPosition import MaskPosition

class setStickerMaskPosition:
    async def set_sticker_mask_position(
        self,
        sticker : str = None,
        mask_position : MaskPosition = None,
    ):
        """
        Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success.

        Args:
            sticker (str): File identifier of the sticker.

            mask_position (MaskPosition): A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position..
        """

        return await Curl.request(
            url=self.api + "setStickerMaskPosition",
            json={
                "sticker": sticker,
                "mask_position": mask_position,
            }
        )
