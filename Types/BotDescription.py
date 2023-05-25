from .utils import *
import Types

class BotDescription(TelegramObject):
    """
    This object represents the bot's description.

    Args:
        description (str): The bot's description.
    """   
    def __init__(
        self: TelegramObject,
        description : str = None,
    ):
        self.update(locals())
