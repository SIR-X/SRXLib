from .utils import *
import Types

class InlineQueryResultCachedAudio(TelegramObject):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be audio.

        id (str): Unique identifier for this result, 1-64 bytes.

        audio_file_id (str): A valid file identifier for the audio file.

        caption (str): Optional. Caption, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the audio caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the audio.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        audio_file_id : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
