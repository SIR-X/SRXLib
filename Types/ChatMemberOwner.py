from .utils import *
import Types

class ChatMemberOwner(TelegramType):
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    Args:
        status (str): The member's status in the chat, always “creator”.

        user ("Types.User"): Information about the user.

        is_anonymous (bool): True, if the user's presence in the chat is hidden.

        custom_title (str): Optional. Custom title for this user.
    """   
    def __init__(
        self: TelegramType,
        status : str = None,
        user : "Types.User" = None,
        is_anonymous : bool = None,
        custom_title : str = None,
    ):
        self.update(locals())
