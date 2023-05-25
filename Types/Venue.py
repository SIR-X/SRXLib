from .utils import *
import Types

class Venue(TelegramObject):
    """
    This object represents a venue.

    Args:
        location (Location): Venue location. Can't be a live location.

        title (str): Name of the venue.

        address (str): Address of the venue.

        foursquare_id (str): Optional. Foursquare identifier of the venue.

        foursquare_type (str): Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.).

        google_place_id (str): Optional. Google Places identifier of the venue.

        google_place_type (str): Optional. Google Places type of the venue. (See supported types.).
    """   
    def __init__(
        self: TelegramObject,
        location : "Types.Location" = None,
        title : str = None,
        address : str = None,
        foursquare_id : str = None,
        foursquare_type : str = None,
        google_place_id : str = None,
        google_place_type : str = None,
    ):
        self.update(locals())
