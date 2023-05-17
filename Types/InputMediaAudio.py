from .utils import *
import Types

class InputMediaAudio(TelegramType):
    """
    Represents an audio file to be treated as music to be sent.

    Args:
        type (str): Type of the result, must be audio.

        media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files ».

        thumbnail ("Types.InputFile | str"): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files ».

        caption (str): Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the audio caption. See formatting options for more details..

        caption_entities (list["Types.MessageEntity"]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        duration (int): Optional. Duration of the audio in seconds.

        performer (str): Optional. Performer of the audio.

        title (str): Optional. Title of the audio.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        media : str = None,
        thumbnail : "Types.InputFile | str" = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        duration : int = None,
        performer : str = None,
        title : str = None,
    ):
        self.update(locals())
