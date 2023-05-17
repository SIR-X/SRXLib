from .utils import *
import Types

class BotName(TelegramType):
    """
    This object represents the bot's name.

    Args:
        name (str): The bot's name.
    """   
    def __init__(
        self: TelegramType,
        name : str = None,
    ):
        self.update(locals())
