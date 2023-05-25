from .utils import *
import Types

class InlineQueryResultLocation(TelegramObject):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be location.

        id (str): Unique identifier for this result, 1-64 Bytes.

        latitude (float): Location latitude in degrees.

        longitude (float): Location longitude in degrees.

        title (str): Location title.

        horizontal_accuracy (float): Optional. The radius of uncertainty for the location, measured in meters; 0-1500.

        live_period (int): Optional. Period in seconds for which the location can be updated, should be between 60 and 86400..

        heading (int): Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified..

        proximity_alert_radius (int): Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified..

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message.

        input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the location.

        thumbnail_url (str): Optional. Url of the thumbnail for the result.

        thumbnail_width (int): Optional. Thumbnail width.

        thumbnail_height (int): Optional. Thumbnail height.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        id : str = None,
        latitude : float = None,
        longitude : float = None,
        title : str = None,
        horizontal_accuracy : float = None,
        live_period : int = None,
        heading : int = None,
        proximity_alert_radius : int = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
        thumbnail_url : str = None,
        thumbnail_width : int = None,
        thumbnail_height : int = None,
    ):
        self.update(locals())
