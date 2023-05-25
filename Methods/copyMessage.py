from .utils import *
import typing
from Types.MessageEntity import MessageEntity
from Types.ForceReply import ForceReply
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove

class copyMessage:
    async def copy_message(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        from_chat_id : typing.Union[int, str] = None,
        message_id : int = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list[MessageEntity] = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : typing.Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
    ):
        """
        Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            from_chat_id (int | str): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

            message_id (int): Message identifier in the chat specified in from_chat_id.

            caption (str): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept.

            parse_mode (str): Mode for parsing entities in the new caption. See formatting options for more details..

            caption_entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "copyMessage",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "from_chat_id": from_chat_id,
                "message_id": message_id,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": caption_entities,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
