from .utils import *
import Types

class BotCommandScopeDefault(TelegramObject):
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    Args:
        type (str): Scope type, must be default.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
    ):
        self.update(locals())
