from .utils import *
import Types

class InlineQueryResultCachedVideo(TelegramType):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Args:
        type (str): Type of the result, must be video.

        id (str): Unique identifier for this result, 1-64 bytes.

        video_file_id (str): A valid file identifier for the video file.

        title (str): Title for the result.

        description (str): Optional. Short description of the result.

        caption (str): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the video caption. See formatting options for more details..

        caption_entities (list["Types.MessageEntity"]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup ("Types.InlineKeyboardMarkup"): Optional. Inline keyboard attached to the message.

        input_message_content ("Types.InputMessageContent"): Optional. Content of the message to be sent instead of the video.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        id : str = None,
        video_file_id : str = None,
        title : str = None,
        description : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
