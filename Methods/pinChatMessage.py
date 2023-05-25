from .utils import *
import typing


class pinChatMessage:
    async def pin_chat_message(
        self,
        chat_id : typing.Union[int, str] = None,
        message_id : int = None,
        disable_notification : bool = None,
    ):
        """
        Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Identifier of a message to pin.

            disable_notification (bool): Pass True if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats..
        """

        return await Curl.request(
            url=self.api + "pinChatMessage",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "disable_notification": disable_notification,
            }
        )
