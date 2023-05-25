from .utils import *
import Types

class ForumTopicEdited(TelegramObject):
    """
    This object represents a service message about an edited forum topic.

    Args:
        name (str): Optional. New name of the topic, if it was edited.

        icon_custom_emoji_id (str): Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed.
    """   
    def __init__(
        self: TelegramObject,
        name : str = None,
        icon_custom_emoji_id : str = None,
    ):
        self.update(locals())
