from .utils import *
import Types

class ChatPermissions(TelegramObject):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    Args:
        can_send_messages (bool): Optional. True, if the user is allowed to send text messages, contacts, invoices, locations and venues.

        can_send_audios (bool): Optional. True, if the user is allowed to send audios.

        can_send_documents (bool): Optional. True, if the user is allowed to send documents.

        can_send_photos (bool): Optional. True, if the user is allowed to send photos.

        can_send_videos (bool): Optional. True, if the user is allowed to send videos.

        can_send_video_notes (bool): Optional. True, if the user is allowed to send video notes.

        can_send_voice_notes (bool): Optional. True, if the user is allowed to send voice notes.

        can_send_polls (bool): Optional. True, if the user is allowed to send polls.

        can_send_other_messages (bool): Optional. True, if the user is allowed to send animations, games, stickers and use inline bots.

        can_add_web_page_previews (bool): Optional. True, if the user is allowed to add web page previews to their messages.

        can_change_info (bool): Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.

        can_invite_users (bool): Optional. True, if the user is allowed to invite new users to the chat.

        can_pin_messages (bool): Optional. True, if the user is allowed to pin messages. Ignored in public supergroups.

        can_manage_topics (bool): Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages.
    """   
    def __init__(
        self: TelegramObject,
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
    ):
        self.update(locals())
