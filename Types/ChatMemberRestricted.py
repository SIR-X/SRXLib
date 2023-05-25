from .utils import *
import Types

class ChatMemberRestricted(TelegramObject):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.

    Args:
        status (str): The member's status in the chat, always “restricted”.

        user (User): Information about the user.

        is_member (bool): True, if the user is a member of the chat at the moment of the request.

        can_send_messages (bool): True, if the user is allowed to send text messages, contacts, invoices, locations and venues.

        can_send_audios (bool): True, if the user is allowed to send audios.

        can_send_documents (bool): True, if the user is allowed to send documents.

        can_send_photos (bool): True, if the user is allowed to send photos.

        can_send_videos (bool): True, if the user is allowed to send videos.

        can_send_video_notes (bool): True, if the user is allowed to send video notes.

        can_send_voice_notes (bool): True, if the user is allowed to send voice notes.

        can_send_polls (bool): True, if the user is allowed to send polls.

        can_send_other_messages (bool): True, if the user is allowed to send animations, games, stickers and use inline bots.

        can_add_web_page_previews (bool): True, if the user is allowed to add web page previews to their messages.

        can_change_info (bool): True, if the user is allowed to change the chat title, photo and other settings.

        can_invite_users (bool): True, if the user is allowed to invite new users to the chat.

        can_pin_messages (bool): True, if the user is allowed to pin messages.

        can_manage_topics (bool): True, if the user is allowed to create forum topics.

        until_date (int): Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever.
    """   
    def __init__(
        self: TelegramObject,
        status : str = None,
        user : "Types.User" = None,
        is_member : bool = None,
        can_send_messages : bool = None,
        can_send_audios : bool = None,
        can_send_documents : bool = None,
        can_send_photos : bool = None,
        can_send_videos : bool = None,
        can_send_video_notes : bool = None,
        can_send_voice_notes : bool = None,
        can_send_polls : bool = None,
        can_send_other_messages : bool = None,
        can_add_web_page_previews : bool = None,
        can_change_info : bool = None,
        can_invite_users : bool = None,
        can_pin_messages : bool = None,
        can_manage_topics : bool = None,
        until_date : int = None,
    ):
        self.update(locals())
