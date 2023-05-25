from .utils import *
import typing


class banChatMember:
    async def ban_chat_member(
        self,
        chat_id : typing.Union[int, str] = None,
        user_id : int = None,
        until_date : int = None,
        revoke_messages : bool = None,
    ):
        """
        Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername).

            user_id (int): Unique identifier of the target user.

            until_date (int): Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only..

            revoke_messages (bool): Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels..
        """

        return await Curl.request(
            url=self.api + "banChatMember",
            json={
                "chat_id": chat_id,
                "user_id": user_id,
                "until_date": until_date,
                "revoke_messages": revoke_messages,
            }
        )
