from .utils import *
import typing
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class editMessageLiveLocation:
    async def edit_message_live_location(
        self,
        chat_id : typing.Union[int, str] = None,
        message_id : int = None,
        inline_message_id : str = None,
        latitude : float = None,
        longitude : float = None,
        horizontal_accuracy : float = None,
        heading : int = None,
        proximity_alert_radius : int = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.

            latitude (float): Latitude of new location.

            longitude (float): Longitude of new location.

            horizontal_accuracy (float): The radius of uncertainty for the location, measured in meters; 0-1500.

            heading (int): Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified..

            proximity_alert_radius (int): The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified..

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for a new inline keyboard..
        """

        return await Curl.request(
            url=self.api + "editMessageLiveLocation",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "latitude": latitude,
                "longitude": longitude,
                "horizontal_accuracy": horizontal_accuracy,
                "heading": heading,
                "proximity_alert_radius": proximity_alert_radius,
                "reply_markup": reply_markup,
            }
        )
