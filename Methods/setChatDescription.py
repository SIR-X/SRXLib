from .utils import *


class setChatDescription:
    async def set_chat_description(
        self,
        chat_id : int | str = None,
        description : str = None,
    ):
        """
        Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            description (str): New chat description, 0-255 characters.
        """

        return await Curl.request(
            url=api + "setChatDescription",
            json={
                "chat_id": chat_id,
                "description": description,
            }
        )
