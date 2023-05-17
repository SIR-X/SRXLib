from .utils import *
import Types

class ProximityAlertTriggered(TelegramType):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Args:
        traveler ("Types.User"): User that triggered the alert.

        watcher ("Types.User"): User that set the alert.

        distance (int): The distance between the users.
    """   
    def __init__(
        self: TelegramType,
        traveler : "Types.User" = None,
        watcher : "Types.User" = None,
        distance : int = None,
    ):
        self.update(locals())
