from .utils import *
import Types

class BotShortDescription(TelegramType):
    """
    This object represents the bot's short description.

    Args:
        short_description (str): The bot's short description.
    """   
    def __init__(
        self: TelegramType,
        short_description : str = None,
    ):
        self.update(locals())
