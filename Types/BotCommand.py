from .utils import *
import Types

class BotCommand(TelegramType):
    """
    This object represents a bot command.

    Args:
        command (str): Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores..

        description (str): Description of the command; 1-256 characters..
    """   
    def __init__(
        self: TelegramType,
        command : str = None,
        description : str = None,
    ):
        self.update(locals())
