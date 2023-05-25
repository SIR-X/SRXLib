from .utils import *
import Types, typing

class VideoNote(TelegramObject):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    Args:
        file_id (str): Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..

        length (int): Video width and height (diameter of the video message) as defined by sender.

        duration (int): Duration of the video in seconds as defined by sender.

        thumbnail (PhotoSize): Optional. Video thumbnail.

        file_size (int): Optional. File size in bytes.
    """   
    def __init__(
        self: TelegramObject,
        file_id : str = None,
        file_unique_id : str = None,
        length : int = None,
        duration : int = None,
        thumbnail : "Types.PhotoSize" = None,
        file_size : int = None,
    ):
        self.update(locals())
