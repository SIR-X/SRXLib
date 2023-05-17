from .utils import *
import Types

class BotDescription(TelegramType):
    """
    This object represents the bot's description.

    Args:
        description (str): The bot's description.
    """   
    def __init__(
        self: TelegramType,
        description : str = None,
    ):
        self.update(locals())
