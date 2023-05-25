from .utils import *


class revokeChatInviteLink:
    async def revoke_chat_invite_link(
        self,
        chat_id : int | str = None,
        invite_link : str = None,
    ):
        """
        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.

        Args:
            chat_id (int | str): Unique identifier of the target chat or username of the target channel (in the format @channelusername).

            invite_link (str): The invite link to revoke.
        """

        return await Curl.request(
            url=self.api + "revokeChatInviteLink",
            json={
                "chat_id": chat_id,
                "invite_link": invite_link,
            }
        )
