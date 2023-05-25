from .utils import *
import Types, typing

class InputTextMessageContent(TelegramObject):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Args:
        message_text (str): Text of the message to be sent, 1-4096 characters.

        parse_mode (str): Optional. Mode for parsing entities in the message text. See formatting options for more details..

        entities (list[MessageEntity]): Optional. List of special entities that appear in message text, which can be specified instead of parse_mode.

        disable_web_page_preview (bool): Optional. Disables link previews for links in the sent message.
    """   
    def __init__(
        self: TelegramObject,
        message_text : str = None,
        parse_mode : str = None,
        entities : list["Types.MessageEntity"] = None,
        disable_web_page_preview : bool = None,
    ):
        self.update(locals())
