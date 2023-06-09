from .utils import *
import typing
from Types.ChatPermissions import ChatPermissions

class restrictChatMember:
    async def restrict_chat_member(
        self,
        chat_id : typing.Union[int, str] = None,
        user_id : int = None,
        permissions : ChatPermissions = None,
        use_independent_chat_permissions : bool = None,
        until_date : int = None,
    ):
        """
        Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            user_id (int): Unique identifier of the target user.

            permissions (ChatPermissions): A JSON-serialized object for new user permissions.

            use_independent_chat_permissions (bool): Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission..

            until_date (int): Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever.
        """

        return await Curl.request(
            url=self.api + "restrictChatMember",
            json={
                "chat_id": chat_id,
                "user_id": user_id,
                "permissions": permissions,
                "use_independent_chat_permissions": use_independent_chat_permissions,
                "until_date": until_date,
            }
        )
