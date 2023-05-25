from .utils import *
import Types, typing

class MaskPosition(TelegramObject):
    """
    This object describes the position on faces where a mask should be placed by default.

    Args:
        point (str): The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”..

        x_shift (float): Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position..

        y_shift (float): Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position..

        scale (float): Mask scaling coefficient. For example, 2.0 means double size..
    """   
    def __init__(
        self: TelegramObject,
        point : str = None,
        x_shift : float = None,
        y_shift : float = None,
        scale : float = None,
    ):
        self.update(locals())
