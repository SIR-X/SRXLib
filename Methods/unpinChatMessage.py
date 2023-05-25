from .utils import *


class unpinChatMessage:
    async def unpin_chat_message(
        self,
        chat_id : int | str = None,
        message_id : int = None,
    ):
        """
        Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned..
        """

        return await Curl.request(
            url=self.api + "unpinChatMessage",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )
