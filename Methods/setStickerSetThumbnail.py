from .utils import *
from Types.InputFile import InputFile

class setStickerSetThumbnail:
    async def set_sticker_set_thumbnail(
        self,
        name : str = None,
        user_id : int = None,
        thumbnail : InputFile | str = None,
    ):
        """
        Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns True on success.

        Args:
            name (str): Sticker set name.

            user_id (int): User identifier of the sticker set owner.

            thumbnail (InputFile | str): A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation with a thumbnail up to 32 kilobytes in size (see https://core.tlgr.org/stickers#animated-sticker-requirements for animated sticker technical requirements), or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.tlgr.org/stickers#video-sticker-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files ». Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail..
        """

        return await Curl.request(
            url=api + "setStickerSetThumbnail",
            json={
                "name": name,
                "user_id": user_id,
                "thumbnail": thumbnail,
            }
        )
