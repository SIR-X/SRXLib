from .utils import *


class getChatMemberCount:
    async def get_chat_member_count(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to get the number of members in a chat. Returns Int on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername).
        """

        return await Curl.request(
            url=api + "getChatMemberCount",
            json={
                "chat_id": chat_id,
            }
        )
