from .utils import *
import Types

class ChatPhoto(TelegramType):
    """
    This object represents a chat photo.

    Args:
        small_file_id (str): File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed..

        small_file_unique_id (str): Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..

        big_file_id (str): File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed..

        big_file_unique_id (str): Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..
    """   
    def __init__(
        self: TelegramType,
        small_file_id : str = None,
        small_file_unique_id : str = None,
        big_file_id : str = None,
        big_file_unique_id : str = None,
    ):
        self.update(locals())
