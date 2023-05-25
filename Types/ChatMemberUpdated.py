from .utils import *
import Types

class ChatMemberUpdated(TelegramObject):
    """
    This object represents changes in the status of a chat member.

    Args:
        chat (Chat): Chat the user belongs to.

        _from (User): Performer of the action, which resulted in the change.

        date (int): Date the change was done in Unix time.

        old_chat_member (ChatMember): Previous information about the chat member.

        new_chat_member (ChatMember): New information about the chat member.

        invite_link (ChatInviteLink): Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only..

        via_chat_folder_invite_link (bool): Optional. True, if the user joined the chat via a chat folder invite link.
    """   
    def __init__(
        self: TelegramObject,
        chat : "Types.Chat" = None,
        _from : "Types.User" = None,
        date : int = None,
        old_chat_member : "Types.ChatMember" = None,
        new_chat_member : "Types.ChatMember" = None,
        invite_link : "Types.ChatInviteLink" = None,
        via_chat_folder_invite_link : bool = None,
    ):
        self.update(locals())
