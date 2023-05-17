from .utils import *
import Types

class Game(TelegramType):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Args:
        title (str): Title of the game.

        description (str): Description of the game.

        photo (list["Types.PhotoSize"]): Photo that will be displayed in the game message in chats..

        text (str): Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters..

        text_entities (list["Types.MessageEntity"]): Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc..

        animation ("Types.Animation"): Optional. Animation that will be displayed in the game message in chats. Upload via BotFather.
    """   
    def __init__(
        self: TelegramType,
        title : str = None,
        description : str = None,
        photo : list["Types.PhotoSize"] = None,
        text : str = None,
        text_entities : list["Types.MessageEntity"] = None,
        animation : "Types.Animation" = None,
    ):
        self.update(locals())
