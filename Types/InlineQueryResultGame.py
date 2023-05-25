from .utils import *
import Types

class InlineQueryResultGame(TelegramObject):
    """
    Represents a Game.
    
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    Args:
        type (str): Type of the result, must be game.

        id (str): Unique identifier for this result, 1-64 bytes.

        game_short_name (str): Short name of the game.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        game_short_name : str = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
    ):
        self.update(locals())
