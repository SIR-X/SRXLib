from .utils import *
import Types

class ChatLocation(TelegramObject):
    """
    Represents a location to which a chat is connected.

    Args:
        location (Location): The location to which the supergroup is connected. Can't be a live location..

        address (str): Location address; 1-64 characters, as defined by the chat owner.
    """   
    def __init__(
        self: TelegramObject,
        location : "Types.Location" = None,
        address : str = None,
    ):
        self.update(locals())
