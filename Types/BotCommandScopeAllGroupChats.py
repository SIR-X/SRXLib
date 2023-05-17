from .utils import *
import Types

class BotCommandScopeAllGroupChats(TelegramType):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    Args:
        type (str): Scope type, must be all_group_chats.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
    ):
        self.update(locals())
