from .utils import *
import Types

class MenuButtonDefault(TelegramObject):
    """
    Describes that no specific value for the menu button was set.

    Args:
        type (str): Type of the button, must be default.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
    ):
        self.update(locals())
