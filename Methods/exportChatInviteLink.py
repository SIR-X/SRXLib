from .utils import *
import typing


class exportChatInviteLink:
    async def export_chat_invite_link(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
        """

        return await Curl.request(
            url=self.api + "exportChatInviteLink",
            json={
                "chat_id": chat_id,
            }
        )
