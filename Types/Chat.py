from .utils import *
import Types, typing

class Chat(TelegramObject):
    """
    This object represents a chat.

    Args:
        id (int): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier..

        type (str): Type of chat, can be either “private”, “group”, “supergroup” or “channel”.

        title (str): Optional. Title, for supergroups, channels and group chats.

        username (str): Optional. Username, for private chats, supergroups and channels if available.

        first_name (str): Optional. First name of the other party in a private chat.

        last_name (str): Optional. Last name of the other party in a private chat.

        is_forum (bool): Optional. True, if the supergroup chat is a forum (has topics enabled).

        photo (ChatPhoto): Optional. Chat photo. Returned only in getChat..

        active_usernames (list[str]): Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat..

        emoji_status_custom_emoji_id (str): Optional. Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat..

        bio (str): Optional. Bio of the other party in a private chat. Returned only in getChat..

        has_private_forwards (bool): Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat..

        has_restricted_voice_and_video_messages (bool): Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat..

        join_to_send_messages (bool): Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat..

        join_by_request (bool): Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat..

        description (str): Optional. Description, for groups, supergroups and channel chats. Returned only in getChat..

        invite_link (str): Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat..

        pinned_message (Message): Optional. The most recent pinned message (by sending date). Returned only in getChat..

        permissions (ChatPermissions): Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat..

        slow_mode_delay (int): Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat..

        message_auto_delete_time (int): Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat..

        has_aggressive_anti_spam_enabled (bool): Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat..

        has_hidden_members (bool): Optional. True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat..

        has_protected_content (bool): Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat..

        sticker_set_name (str): Optional. For supergroups, name of group sticker set. Returned only in getChat..

        can_set_sticker_set (bool): Optional. True, if the bot can change the group sticker set. Returned only in getChat..

        linked_chat_id (int): Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat..

        location (ChatLocation): Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat..
    """   
    def __init__(
        self: TelegramObject,
        id : int = None,
        type : str = None,
        title : str = None,
        username : str = None,
        first_name : str = None,
        last_name : str = None,
        is_forum : bool = None,
        photo : "Types.ChatPhoto" = None,
        active_usernames : list[str] = None,
        emoji_status_custom_emoji_id : str = None,
        bio : str = None,
        has_private_forwards : bool = None,
        has_restricted_voice_and_video_messages : bool = None,
        join_to_send_messages : bool = None,
        join_by_request : bool = None,
        description : str = None,
        invite_link : str = None,
        pinned_message : "Types.Message" = None,
        permissions : "Types.ChatPermissions" = None,
        slow_mode_delay : int = None,
        message_auto_delete_time : int = None,
        has_aggressive_anti_spam_enabled : bool = None,
        has_hidden_members : bool = None,
        has_protected_content : bool = None,
        sticker_set_name : str = None,
        can_set_sticker_set : bool = None,
        linked_chat_id : int = None,
        location : "Types.ChatLocation" = None,
    ):
        self.update(locals())
