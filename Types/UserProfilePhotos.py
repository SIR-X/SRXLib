from .utils import *
import Types

class UserProfilePhotos(TelegramObject):
    """
    This object represent a user's profile pictures.

    Args:
        total_count (int): Total number of profile pictures the target user has.

        photos (list[list[PhotoSize]]): Requested profile pictures (in up to 4 sizes each).
    """   
    def __init__(
        self: TelegramObject,
        total_count : int = None,
        photos : list[list["Types.PhotoSize"]] = None,
    ):
        self.update(locals())
