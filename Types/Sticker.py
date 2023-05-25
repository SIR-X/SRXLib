from .utils import *
import Types

class Sticker(TelegramObject):
    """
    This object represents a sticker.

    Args:
        file_id (str): Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..

        type (str): Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video..

        width (int): Sticker width.

        height (int): Sticker height.

        is_animated (bool): True, if the sticker is animated.

        is_video (bool): True, if the sticker is a video sticker.

        thumbnail (PhotoSize): Optional. Sticker thumbnail in the .WEBP or .JPG format.

        emoji (str): Optional. Emoji associated with the sticker.

        set_name (str): Optional. Name of the sticker set to which the sticker belongs.

        premium_animation (File): Optional. For premium regular stickers, premium animation for the sticker.

        mask_position (MaskPosition): Optional. For mask stickers, the position where the mask should be placed.

        custom_emoji_id (str): Optional. For custom emoji stickers, unique identifier of the custom emoji.

        needs_repainting (bool): Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places.

        file_size (int): Optional. File size in bytes.
    """   
    def __init__(
        self: TelegramObject,
        file_id : str = None,
        file_unique_id : str = None,
        type : str = None,
        width : int = None,
        height : int = None,
        is_animated : bool = None,
        is_video : bool = None,
        thumbnail : "Types.PhotoSize" = None,
        emoji : str = None,
        set_name : str = None,
        premium_animation : "Types.File" = None,
        mask_position : "Types.MaskPosition" = None,
        custom_emoji_id : str = None,
        needs_repainting : bool = None,
        file_size : int = None,
    ):
        self.update(locals())
