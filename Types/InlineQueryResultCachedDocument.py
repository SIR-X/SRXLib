from .utils import *
import Types

class InlineQueryResultCachedDocument(TelegramObject):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be document.

        id (str): Unique identifier for this result, 1-64 bytes.

        title (str): Title for the result.

        document_file_id (str): A valid file identifier for the file.

        description (str): Optional. Short description of the result.

        caption (str): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the document caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the file.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        title : str = None,
        document_file_id : str = None,
        description : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
