from .utils import *
import Types, typing

class Poll(TelegramObject):
    """
    This object contains information about a poll.

    Args:
        id (str): Unique poll identifier.

        question (str): Poll question, 1-300 characters.

        options (list[PollOption]): List of poll options.

        total_voter_count (int): Total number of users that voted in the poll.

        is_closed (bool): True, if the poll is closed.

        is_anonymous (bool): True, if the poll is anonymous.

        type (str): Poll type, currently can be “regular” or “quiz”.

        allows_multiple_answers (bool): True, if the poll allows multiple answers.

        correct_option_id (int): Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot..

        explanation (str): Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters.

        explanation_entities (list[MessageEntity]): Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation.

        open_period (int): Optional. Amount of time in seconds the poll will be active after creation.

        close_date (int): Optional. Point in time (Unix timestamp) when the poll will be automatically closed.
    """   
    def __init__(
        self: TelegramObject,
        id : str = None,
        question : str = None,
        options : list["Types.PollOption"] = None,
        total_voter_count : int = None,
        is_closed : bool = None,
        is_anonymous : bool = None,
        type : str = None,
        allows_multiple_answers : bool = None,
        correct_option_id : int = None,
        explanation : str = None,
        explanation_entities : list["Types.MessageEntity"] = None,
        open_period : int = None,
        close_date : int = None,
    ):
        self.update(locals())
