from .utils import *


class unbanChatSenderChat:
    async def unban_chat_sender_chat(
        self,
        chat_id : int | str = None,
        sender_chat_id : int = None,
    ):
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            sender_chat_id (int): Unique identifier of the target sender chat.
        """

        return await Curl.request(
            url=self.api + "unbanChatSenderChat",
            json={
                "chat_id": chat_id,
                "sender_chat_id": sender_chat_id,
            }
        )
