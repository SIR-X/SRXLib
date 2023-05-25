from .utils import *
import Types

class PollAnswer(TelegramObject):
    """
    This object represents an answer of a user in a non-anonymous poll.

    Args:
        poll_id (str): Unique poll identifier.

        user (User): The user, who changed the answer to the poll.

        option_ids (list[int]): 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote..
    """   
    def __init__(
        self: TelegramObject,
        poll_id : str = None,
        user : "Types.User" = None,
        option_ids : list[int] = None,
    ):
        self.update(locals())
