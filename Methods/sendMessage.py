from .utils import *
import typing
from Types.MessageEntity import MessageEntity
from Types.ForceReply import ForceReply
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove

class sendMessage:
    async def send_message(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        text : str = None,
        parse_mode : str = None,
        entities : list[MessageEntity] = None,
        disable_web_page_preview : bool = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : typing.Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
    ):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            text (str): Text of the message to be sent, 1-4096 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the message text. See formatting options for more details..

            entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode.

            disable_web_page_preview (bool): Disables link previews for links in this message.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendMessage",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "text": text,
                "parse_mode": parse_mode,
                "entities": entities,
                "disable_web_page_preview": disable_web_page_preview,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
