from .utils import *
from Types.InputFile import InputFile

class uploadStickerFile:
    async def upload_sticker_file(
        self,
        user_id : int = None,
        sticker : InputFile = None,
        sticker_format : str = None,
    ):
        """
        Use this method to upload a file with a sticker for later use in the createNewStickerSet and addStickerToSet methods (the file can be used multiple times). Returns the uploaded File on success.

        Args:
            user_id (int): User identifier of sticker file owner.

            sticker (InputFile): A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.tlgr.org/stickers for technical requirements. More information on Sending Files ».

            sticker_format (str): Format of the sticker, must be one of “static”, “animated”, “video”.
        """

        return await Curl.request(
            url=self.api + "uploadStickerFile",
            json={
                "user_id": user_id,
                "sticker": sticker,
                "sticker_format": sticker_format,
            }
        )
