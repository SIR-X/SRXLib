from .utils import *
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove
from Types.ForceReply import ForceReply
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class sendVenue:
    async def send_venue(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        latitude : float = None,
        longitude : float = None,
        title : str = None,
        address : str = None,
        foursquare_id : str = None,
        foursquare_type : str = None,
        google_place_id : str = None,
        google_place_type : str = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
    ):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            latitude (float): Latitude of the venue.

            longitude (float): Longitude of the venue.

            title (str): Name of the venue.

            address (str): Address of the venue.

            foursquare_id (str): Foursquare identifier of the venue.

            foursquare_type (str): Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.).

            google_place_id (str): Google Places identifier of the venue.

            google_place_type (str): Google Places type of the venue. (See supported types.).

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendVenue",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "latitude": latitude,
                "longitude": longitude,
                "title": title,
                "address": address,
                "foursquare_id": foursquare_id,
                "foursquare_type": foursquare_type,
                "google_place_id": google_place_id,
                "google_place_type": google_place_type,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
