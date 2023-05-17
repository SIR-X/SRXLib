from .utils import *
import Types

class StickerSet(TelegramType):
    """
    This object represents a sticker set.

    Args:
        name (str): Sticker set name.

        title (str): Sticker set title.

        sticker_type (str): Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”.

        is_animated (bool): True, if the sticker set contains animated stickers.

        is_video (bool): True, if the sticker set contains video stickers.

        stickers (list["Types.Sticker"]): List of all set stickers.

        thumbnail ("Types.PhotoSize"): Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format.
    """   
    def __init__(
        self: TelegramType,
        name : str = None,
        title : str = None,
        sticker_type : str = None,
        is_animated : bool = None,
        is_video : bool = None,
        stickers : list["Types.Sticker"] = None,
        thumbnail : "Types.PhotoSize" = None,
    ):
        self.update(locals())
