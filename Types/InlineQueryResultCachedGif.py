from .utils import *
import Types, typing

class InlineQueryResultCachedGif(TelegramObject):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    Args:
        type (str): Type of the result, must be gif.

        id (str): Unique identifier for this result, 1-64 bytes.

        gif_file_id (str): A valid file identifier for the GIF file.

        title (str): Optional. Title for the result.

        caption (str): Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the GIF animation.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        gif_file_id : str = None,
        title : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
