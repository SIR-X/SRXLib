from .utils import *
import Types

class InlineKeyboardMarkup(TelegramObject):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    Args:
        inline_keyboard (list[list[InlineKeyboardButton]]): Array of button rows, each represented by an Array of InlineKeyboardButton objects.
    """   
    def __init__(
        self: TelegramObject,
        inline_keyboard : list[list["Types.InlineKeyboardButton"]] = None,
    ):
        self.update(locals())
