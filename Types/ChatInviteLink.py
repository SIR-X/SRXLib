from .utils import *
import Types

class ChatInviteLink(TelegramType):
    """
    Represents an invite link for a chat.

    Args:
        invite_link (str): The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”..

        creator ("Types.User"): Creator of the link.

        creates_join_request (bool): True, if users joining the chat via the link need to be approved by chat administrators.

        is_primary (bool): True, if the link is primary.

        is_revoked (bool): True, if the link is revoked.

        name (str): Optional. Invite link name.

        expire_date (int): Optional. Point in time (Unix timestamp) when the link will expire or has been expired.

        member_limit (int): Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.

        pending_join_request_count (int): Optional. Number of pending join requests created using this link.
    """   
    def __init__(
        self: TelegramType,
        invite_link : str = None,
        creator : "Types.User" = None,
        creates_join_request : bool = None,
        is_primary : bool = None,
        is_revoked : bool = None,
        name : str = None,
        expire_date : int = None,
        member_limit : int = None,
        pending_join_request_count : int = None,
    ):
        self.update(locals())
