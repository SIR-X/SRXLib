from .utils import *
import Types, typing

class InlineQueryResultMpeg4Gif(TelegramObject):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Args:
        type (str): Type of the result, must be mpeg4_gif.

        id (str): Unique identifier for this result, 1-64 bytes.

        mpeg4_url (str): A valid URL for the MPEG4 file. File size must not exceed 1MB.

        mpeg4_width (int): Optional. Video width.

        mpeg4_height (int): Optional. Video height.

        mpeg4_duration (int): Optional. Video duration in seconds.

        thumbnail_url (str): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result.

        thumbnail_mime_type (str): Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”.

        title (str): Optional. Title for the result.

        caption (str): Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing.

        parse_mode (str): Optional. Mode for parsing entities in the caption. See formatting options for more details..

        caption_entities (list[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video animation.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        mpeg4_url : str = None,
        mpeg4_width : int = None,
        mpeg4_height : int = None,
        mpeg4_duration : int = None,
        thumbnail_url : str = None,
        thumbnail_mime_type : str = None,
        title : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
    ):
        self.update(locals())
