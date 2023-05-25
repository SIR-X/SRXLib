from .utils import *
import Types, typing

class BotCommandScopeChatAdministrators(TelegramObject):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    Args:
        type (str): Scope type, must be chat_administrators.

        chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        chat_id : typing.Union[int, str] = None,
    ):
        self.update(locals())
