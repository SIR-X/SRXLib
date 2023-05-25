from .utils import *


class deleteChatPhoto:
    async def delete_chat_photo(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "deleteChatPhoto",
            json={
                "chat_id": chat_id,
            }
        )
