from .utils import *
import Types

class UserProfilePhotos(TelegramType):
    """
    This object represent a user's profile pictures.

    Args:
        total_count (int): Total number of profile pictures the target user has.

        photos (list[list["Types.PhotoSize"]]): Requested profile pictures (in up to 4 sizes each).
    """   
    def __init__(
        self: TelegramType,
        total_count : int = None,
        photos : list[list["Types.PhotoSize"]] = None,
    ):
        self.update(locals())
