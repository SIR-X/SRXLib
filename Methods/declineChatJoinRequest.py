from .utils import *


class declineChatJoinRequest:
    async def decline_chat_join_request(
        self,
        chat_id : int | str = None,
        user_id : int = None,
    ):
        """
        Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int): Unique identifier of the target user.
        """

        return await Curl.request(
            url=self.api + "declineChatJoinRequest",
            json={
                "chat_id": chat_id,
                "user_id": user_id,
            }
        )
