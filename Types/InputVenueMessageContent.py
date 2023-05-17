from .utils import *
import Types

class InputVenueMessageContent(TelegramType):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Args:
        latitude (float): Latitude of the venue in degrees.

        longitude (float): Longitude of the venue in degrees.

        title (str): Name of the venue.

        address (str): Address of the venue.

        foursquare_id (str): Optional. Foursquare identifier of the venue, if known.

        foursquare_type (str): Optional. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.).

        google_place_id (str): Optional. Google Places identifier of the venue.

        google_place_type (str): Optional. Google Places type of the venue. (See supported types.).
    """   
    def __init__(
        self: TelegramType,
        latitude : float = None,
        longitude : float = None,
        title : str = None,
        address : str = None,
        foursquare_id : str = None,
        foursquare_type : str = None,
        google_place_id : str = None,
        google_place_type : str = None,
    ):
        self.update(locals())
