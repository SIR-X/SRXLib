from .utils import *
import Types

class MenuButtonCommands(TelegramType):
    """
    Represents a menu button, which opens the bot's list of commands.

    Args:
        type (str): Type of the button, must be commands.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
    ):
        self.update(locals())
