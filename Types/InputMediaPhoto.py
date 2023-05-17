from .utils import *
import Types

class InputMediaPhoto(TelegramType):
    """
    Represents a photo to be sent.

    Args:
        type (str): Type of the result, must be photo.

        media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files ».

        caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the photo caption. See formatting options for more details..

        caption_entities (list["Types.MessageEntity"]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        has_spoiler (bool): Optional. Pass True if the photo needs to be covered with a spoiler animation.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        media : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        has_spoiler : bool = None,
    ):
        self.update(locals())
