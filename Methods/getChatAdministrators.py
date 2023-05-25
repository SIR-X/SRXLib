from .utils import *
import typing


class getChatAdministrators:
    async def get_chat_administrators(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "getChatAdministrators",
            json={
                "chat_id": chat_id,
            }
        )
