from .utils import *
import Types, typing

class PassportElementErrorUnspecified(TelegramObject):
    """
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    
    Your bot can offer users HTML5 games to play solo or to compete against each other in groups and one-on-one chats. Create games via @BotFather using the /newgame command. Please note that this kind of power requires responsibility: you will need to accept the terms for each game that your bots will be offering.

    Args:
        source (str): Error source, must be unspecified.

        type (str): Type of element of the user's Telegram Passport which has the issue.

        element_hash (str): Base64-encoded element hash.

        message (str): Error message.
    """   
    def __init__(
        self: TelegramObject,
        source : str = None,
        type : str = None,
        element_hash : str = None,
        message : str = None,
    ):
        self.update(locals())
