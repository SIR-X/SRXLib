from .utils import *


class banChatSenderChat:
    async def ban_chat_sender_chat(
        self,
        chat_id : int | str = None,
        sender_chat_id : int = None,
    ):
        """
        Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            sender_chat_id (int): Unique identifier of the target sender chat.
        """

        return await Curl.request(
            url=api + "banChatSenderChat",
            json={
                "chat_id": chat_id,
                "sender_chat_id": sender_chat_id,
            }
        )
