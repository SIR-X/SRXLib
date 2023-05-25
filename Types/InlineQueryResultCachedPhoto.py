from .utils import *
import Types, typing

class InlineQueryResultCachedPhoto(TelegramObject):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Args:
        type (str): Type of the result, must be photo.

        id (str): Unique identifier for this result, 1-64 bytes.

        photo_file_id (str): A valid file identifier of the photo.

        title (str): Optional. Title for the result.

        description (str): Optional. Short description of the result.

        caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the photo caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the photo.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        photo_file_id : str = None,
        title : str = None,
        description : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
