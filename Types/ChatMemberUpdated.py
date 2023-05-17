from .utils import *
import Types

class ChatMemberUpdated(TelegramType):
    """
    This object represents changes in the status of a chat member.

    Args:
        chat ("Types.Chat"): Chat the user belongs to.

        _from ("Types.User"): Performer of the action, which resulted in the change.

        date (int): Date the change was done in Unix time.

        old_chat_member ("Types.ChatMember"): Previous information about the chat member.

        new_chat_member ("Types.ChatMember"): New information about the chat member.

        invite_link ("Types.ChatInviteLink"): Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only..

        via_chat_folder_invite_link (bool): Optional. True, if the user joined the chat via a chat folder invite link.
    """   
    def __init__(
        self: TelegramType,
        chat : "Types.Chat" = None,
        _from : "Types.User" = None,
        date : int = None,
        old_chat_member : "Types.ChatMember" = None,
        new_chat_member : "Types.ChatMember" = None,
        invite_link : "Types.ChatInviteLink" = None,
        via_chat_folder_invite_link : bool = None,
    ):
        self.update(locals())
