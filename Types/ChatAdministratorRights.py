from .utils import *
import Types, typing

class ChatAdministratorRights(TelegramObject):
    """
    Represents the rights of an administrator in a chat.

    Args:
        is_anonymous (bool): True, if the user's presence in the chat is hidden.

        can_manage_chat (bool): True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege.

        can_delete_messages (bool): True, if the administrator can delete messages of other users.

        can_manage_video_chats (bool): True, if the administrator can manage video chats.

        can_restrict_members (bool): True, if the administrator can restrict, ban or unban chat members.

        can_promote_members (bool): True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).

        can_change_info (bool): True, if the user is allowed to change the chat title, photo and other settings.

        can_invite_users (bool): True, if the user is allowed to invite new users to the chat.

        can_post_messages (bool): Optional. True, if the administrator can post in the channel; channels only.

        can_edit_messages (bool): Optional. True, if the administrator can edit messages of other users and can pin messages; channels only.

        can_pin_messages (bool): Optional. True, if the user is allowed to pin messages; groups and supergroups only.

        can_manage_topics (bool): Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only.
    """   
    def __init__(
        self: TelegramObject,
        is_anonymous : bool = None,
        can_manage_chat : bool = None,
        can_delete_messages : bool = None,
        can_manage_video_chats : bool = None,
        can_restrict_members : bool = None,
        can_promote_members : bool = None,
        can_change_info : bool = None,
        can_invite_users : bool = None,
        can_post_messages : bool = None,
        can_edit_messages : bool = None,
        can_pin_messages : bool = None,
        can_manage_topics : bool = None,
    ):
        self.update(locals())
