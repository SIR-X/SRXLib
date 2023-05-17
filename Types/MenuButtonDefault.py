from .utils import *
import Types

class MenuButtonDefault(TelegramType):
    """
    Describes that no specific value for the menu button was set.

    Args:
        type (str): Type of the button, must be default.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
    ):
        self.update(locals())
