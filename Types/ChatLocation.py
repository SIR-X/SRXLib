from .utils import *
import Types

class ChatLocation(TelegramType):
    """
    Represents a location to which a chat is connected.

    Args:
        location ("Types.Location"): The location to which the supergroup is connected. Can't be a live location..

        address (str): Location address; 1-64 characters, as defined by the chat owner.
    """   
    def __init__(
        self: TelegramType,
        location : "Types.Location" = None,
        address : str = None,
    ):
        self.update(locals())
