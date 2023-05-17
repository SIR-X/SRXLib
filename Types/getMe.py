from .utils import *
import Types

class getMe(TelegramType):
    """
    A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

    Args:
        
    """   
    def __init__(
        self: TelegramType,
        
    ):
        self.update(locals())
