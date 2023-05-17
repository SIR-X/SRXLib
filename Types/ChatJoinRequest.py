from .utils import *
import Types

class ChatJoinRequest(TelegramType):
    """
    Represents a join request sent to a chat.

    Args:
        chat ("Types.Chat"): Chat to which the request was sent.

        _from ("Types.User"): User that sent the join request.

        user_chat_id (int): Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages until the join request is processed, assuming no other administrator contacted the user..

        date (int): Date the request was sent in Unix time.

        bio (str): Optional. Bio of the user..

        invite_link ("Types.ChatInviteLink"): Optional. Chat invite link that was used by the user to send the join request.
    """   
    def __init__(
        self: TelegramType,
        chat : "Types.Chat" = None,
        _from : "Types.User" = None,
        user_chat_id : int = None,
        date : int = None,
        bio : str = None,
        invite_link : "Types.ChatInviteLink" = None,
    ):
        self.update(locals())
