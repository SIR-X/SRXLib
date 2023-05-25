from .utils import *
import Types

class Location(TelegramObject):
    """
    This object represents a point on the map.

    Args:
        longitude (float): Longitude as defined by sender.

        latitude (float): Latitude as defined by sender.

        horizontal_accuracy (float): Optional. The radius of uncertainty for the location, measured in meters; 0-1500.

        live_period (int): Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only..

        heading (int): Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only..

        proximity_alert_radius (int): Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only..
    """   
    def __init__(
        self: TelegramObject,
        longitude : float = None,
        latitude : float = None,
        horizontal_accuracy : float = None,
        live_period : int = None,
        heading : int = None,
        proximity_alert_radius : int = None,
    ):
        self.update(locals())
