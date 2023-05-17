from .utils import *
import Types

class BotCommandScopeAllChatAdministrators(TelegramType):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    Args:
        type (str): Scope type, must be all_chat_administrators.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
    ):
        self.update(locals())
