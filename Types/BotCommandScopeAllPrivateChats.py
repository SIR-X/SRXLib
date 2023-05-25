from .utils import *
import Types

class BotCommandScopeAllPrivateChats(TelegramObject):
    """
    Represents the scope of bot commands, covering all private chats.

    Args:
        type (str): Scope type, must be all_private_chats.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
    ):
        self.update(locals())
