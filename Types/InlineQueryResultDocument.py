from .utils import *
import Types

class InlineQueryResultDocument(TelegramObject):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be document.

        id (str): Unique identifier for this result, 1-64 bytes.

        title (str): Title for the result.

        caption (str): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the document caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        document_url (str): A valid URL for the file.

        mime_type (str): MIME type of the content of the file, either “application/pdf” or “application/zip”.

        description (str): Optional. Short description of the result.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the file.

        thumbnail_url (str): Optional. URL of the thumbnail (JPEG only) for the file.

        thumbnail_width (int): Optional. Thumbnail width.

        thumbnail_height (int): Optional. Thumbnail height.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        title : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        document_url : str = None,
        mime_type : str = None,
        description : str = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
        thumbnail_url : str = None,
        thumbnail_width : int = None,
        thumbnail_height : int = None,
    ):
        self.update(locals())
