from .utils import *


class setChatTitle:
    async def set_chat_title(
        self,
        chat_id : int | str = None,
        title : str = None,
    ):
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            title (str): New chat title, 1-128 characters.
        """

        return await Curl.request(
            url=api + "setChatTitle",
            json={
                "chat_id": chat_id,
                "title": title,
            }
        )
