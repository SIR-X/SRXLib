from .utils import *
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove
from Types.ForceReply import ForceReply
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class sendContact:
    async def send_contact(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        phone_number : str = None,
        first_name : str = None,
        last_name : str = None,
        vcard : str = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
    ):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            phone_number (str): Contact's phone number.

            first_name (str): Contact's first name.

            last_name (str): Contact's last name.

            vcard (str): Additional data about the contact in the form of a vCard, 0-2048 bytes.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendContact",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "phone_number": phone_number,
                "first_name": first_name,
                "last_name": last_name,
                "vcard": vcard,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
