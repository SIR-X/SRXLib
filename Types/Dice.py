from .utils import *
import Types

class Dice(TelegramType):
    """
    This object represents an animated emoji that displays a random value.

    Args:
        emoji (str): Emoji on which the dice throw animation is based.

        value (int): Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “” base emoji, 1-64 for “” base emoji.
    """   
    def __init__(
        self: TelegramType,
        emoji : str = None,
        value : int = None,
    ):
        self.update(locals())
