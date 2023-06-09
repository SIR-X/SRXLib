from .utils import *
import typing


class leaveChat:
    async def leave_chat(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "leaveChat",
            json={
                "chat_id": chat_id,
            }
        )
