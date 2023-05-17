from .utils import *
import Types

class InputSticker(TelegramType):
    """
    This object describes a sticker to be added to a sticker set.

    Args:
        sticker ("Types.InputFile | str"): The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files ».

        emoji_list (list[str]): List of 1-20 emoji associated with the sticker.

        mask_position ("Types.MaskPosition"): Optional. Position where the mask should be placed on faces. For “mask” stickers only..

        keywords (list[str]): Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only..
    """   
    def __init__(
        self: TelegramType,
        sticker : "Types.InputFile | str" = None,
        emoji_list : list[str] = None,
        mask_position : "Types.MaskPosition" = None,
        keywords : list[str] = None,
    ):
        self.update(locals())
