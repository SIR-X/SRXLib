from .utils import *
import Types

class BotName(TelegramObject):
    """
    This object represents the bot's name.

    Args:
        name (str): The bot's name.
    """   
    def __init__(
        self: TelegramObject,
        name : str = None,
    ):
        self.update(locals())
