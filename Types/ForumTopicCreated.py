from .utils import *
import Types

class ForumTopicCreated(TelegramType):
    """
    This object represents a service message about a new forum topic created in the chat.

    Args:
        name (str): Name of the topic.

        icon_color (int): Color of the topic icon in RGB format.

        icon_custom_emoji_id (str): Optional. Unique identifier of the custom emoji shown as the topic icon.
    """   
    def __init__(
        self: TelegramType,
        name : str = None,
        icon_color : int = None,
        icon_custom_emoji_id : str = None,
    ):
        self.update(locals())
