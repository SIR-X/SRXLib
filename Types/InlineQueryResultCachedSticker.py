from .utils import *
import Types

class InlineQueryResultCachedSticker(TelegramObject):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be sticker.

        id (str): Unique identifier for this result, 1-64 bytes.

        sticker_file_id (str): A valid file identifier of the sticker.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the sticker.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        sticker_file_id : str = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
