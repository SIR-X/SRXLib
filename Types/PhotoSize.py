from .utils import *
import Types, typing

class PhotoSize(TelegramObject):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    Args:
        file_id (str): Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..

        width (int): Photo width.

        height (int): Photo height.

        file_size (int): Optional. File size in bytes.
    """   
    def __init__(
        self: TelegramObject,
        file_id : str = None,
        file_unique_id : str = None,
        width : int = None,
        height : int = None,
        file_size : int = None,
    ):
        self.update(locals())
