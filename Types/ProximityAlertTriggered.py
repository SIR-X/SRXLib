from .utils import *
import Types, typing

class ProximityAlertTriggered(TelegramObject):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Args:
        traveler (User): User that triggered the alert.

        watcher (User): User that set the alert.

        distance (int): The distance between the users.
    """   
    def __init__(
        self: TelegramObject,
        traveler : "Types.User" = None,
        watcher : "Types.User" = None,
        distance : int = None,
    ):
        self.update(locals())
