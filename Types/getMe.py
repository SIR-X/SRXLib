from .utils import *
import Types

class getMe(TelegramObject):
    """
    A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

    Args:
        
    """   
    def __init__(
        self: TelegramObject,
        
    ):
        self.update(locals())
