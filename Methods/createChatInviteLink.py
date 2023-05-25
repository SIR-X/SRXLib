from .utils import *


class createChatInviteLink:
    async def create_chat_invite_link(
        self,
        chat_id : int | str = None,
        name : str = None,
        expire_date : int = None,
        member_limit : int = None,
        creates_join_request : bool = None,
    ):
        """
        Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            name (str): Invite link name; 0-32 characters.

            expire_date (int): Point in time (Unix timestamp) when the link will expire.

            member_limit (int): The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.

            creates_join_request (bool): True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified.
        """

        return await Curl.request(
            url=self.api + "createChatInviteLink",
            json={
                "chat_id": chat_id,
                "name": name,
                "expire_date": expire_date,
                "member_limit": member_limit,
                "creates_join_request": creates_join_request,
            }
        )
