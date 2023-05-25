from .utils import *
import Types

class Audio(TelegramObject):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    Args:
        file_id (str): Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file..

        duration (int): Duration of the audio in seconds as defined by sender.

        performer (str): Optional. Performer of the audio as defined by sender or by audio tags.

        title (str): Optional. Title of the audio as defined by sender or by audio tags.

        file_name (str): Optional. Original filename as defined by sender.

        mime_type (str): Optional. MIME type of the file as defined by sender.

        file_size (int): Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value..

        thumbnail (PhotoSize): Optional. Thumbnail of the album cover to which the music file belongs.
    """   
    def __init__(
        self: TelegramObject,
        file_id : str = None,
        file_unique_id : str = None,
        duration : int = None,
        performer : str = None,
        title : str = None,
        file_name : str = None,
        mime_type : str = None,
        file_size : int = None,
        thumbnail : "Types.PhotoSize" = None,
    ):
        self.update(locals())
