from .utils import *
import Types, typing

class MenuButtonCommands(TelegramObject):
    """
    Represents a menu button, which opens the bot's list of commands.

    Args:
        type (str): Type of the button, must be commands.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
    ):
        self.update(locals())
