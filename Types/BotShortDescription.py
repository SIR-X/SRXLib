from .utils import *
import Types

class BotShortDescription(TelegramObject):
    """
    This object represents the bot's short description.

    Args:
        short_description (str): The bot's short description.
    """   
    def __init__(
        self: TelegramObject,
        short_description : str = None,
    ):
        self.update(locals())
