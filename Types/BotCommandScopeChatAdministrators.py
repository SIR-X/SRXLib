from .utils import *
import Types

class BotCommandScopeChatAdministrators(TelegramType):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    Args:
        type (str): Scope type, must be chat_administrators.

        chat_id ("Types.int | str"): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        chat_id : "Types.int | str" = None,
    ):
        self.update(locals())
