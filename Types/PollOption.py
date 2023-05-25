from .utils import *
import Types, typing

class PollOption(TelegramObject):
    """
    This object contains information about one answer option in a poll.

    Args:
        text (str): Option text, 1-100 characters.

        voter_count (int): Number of users that voted for this option.
    """   
    def __init__(
        self: TelegramObject,
        text : str = None,
        voter_count : int = None,
    ):
        self.update(locals())
