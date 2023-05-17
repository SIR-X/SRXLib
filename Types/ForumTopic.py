from .utils import *
import Types

class ForumTopic(TelegramType):
    """
    This object represents a forum topic.

    Args:
        message_thread_id (int): Unique identifier of the forum topic.

        name (str): Name of the topic.

        icon_color (int): Color of the topic icon in RGB format.

        icon_custom_emoji_id (str): Optional. Unique identifier of the custom emoji shown as the topic icon.
    """   
    def __init__(
        self: TelegramType,
        message_thread_id : int = None,
        name : str = None,
        icon_color : int = None,
        icon_custom_emoji_id : str = None,
    ):
        self.update(locals())
