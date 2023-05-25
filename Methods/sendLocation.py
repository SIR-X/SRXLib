from .utils import *
import typing
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ForceReply import ForceReply

class sendLocation:
    async def send_location(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        latitude : float = None,
        longitude : float = None,
        horizontal_accuracy : float = None,
        live_period : int = None,
        heading : int = None,
        proximity_alert_radius : int = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : typing.Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
    ):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            latitude (float): Latitude of the location.

            longitude (float): Longitude of the location.

            horizontal_accuracy (float): The radius of uncertainty for the location, measured in meters; 0-1500.

            live_period (int): Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400..

            heading (int): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified..

            proximity_alert_radius (int): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified..

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendLocation",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "latitude": latitude,
                "longitude": longitude,
                "horizontal_accuracy": horizontal_accuracy,
                "live_period": live_period,
                "heading": heading,
                "proximity_alert_radius": proximity_alert_radius,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
