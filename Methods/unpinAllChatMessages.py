from .utils import *
import typing


class unpinAllChatMessages:
    async def unpin_all_chat_messages(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "unpinAllChatMessages",
            json={
                "chat_id": chat_id,
            }
        )
