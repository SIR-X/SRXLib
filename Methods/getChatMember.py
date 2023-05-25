from .utils import *
import typing


class getChatMember:
    async def get_chat_member(
        self,
        chat_id : typing.Union[int, str] = None,
        user_id : int = None,
    ):
        """
        Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername).

            user_id (int): Unique identifier of the target user.
        """

        return await Curl.request(
            url=self.api + "getChatMember",
            json={
                "chat_id": chat_id,
                "user_id": user_id,
            }
        )
