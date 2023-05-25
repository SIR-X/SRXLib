from .utils import *


class getChat:
    async def get_chat(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "getChat",
            json={
                "chat_id": chat_id,
            }
        )
