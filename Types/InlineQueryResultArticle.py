from .utils import *
import Types

class InlineQueryResultArticle(TelegramType):
    """
    Represents a link to an article or web page.

    Args:
        type (str): Type of the result, must be article.

        id (str): Unique identifier for this result, 1-64 Bytes.

        title (str): Title of the result.

        input_message_content ("Types.InputMessageContent"): Content of the message to be sent.

        reply_markup ("Types.InlineKeyboardMarkup"): Optional. Inline keyboard attached to the message.

        url (str): Optional. URL of the result.

        hide_url (bool): Optional. Pass True if you don't want the URL to be shown in the message.

        description (str): Optional. Short description of the result.

        thumbnail_url (str): Optional. Url of the thumbnail for the result.

        thumbnail_width (int): Optional. Thumbnail width.

        thumbnail_height (int): Optional. Thumbnail height.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        id : str = None,
        title : str = None,
        input_message_content : "Types.InputMessageContent" = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        url : str = None,
        hide_url : bool = None,
        description : str = None,
        thumbnail_url : str = None,
        thumbnail_width : int = None,
        thumbnail_height : int = None,
    ):
        self.update(locals())
