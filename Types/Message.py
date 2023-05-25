from .utils import *
import Types, typing

class Message(TelegramObject):
    """
    This object represents a message.

    Args:
        message_id (int): Unique message identifier inside this chat.

        message_thread_id (int): Optional. Unique identifier of a message thread to which the message belongs; for supergroups only.

        _from (User): Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat..

        sender_chat (Chat): Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat..

        date (int): Date the message was sent in Unix time.

        chat (Chat): Conversation the message belongs to.

        forward_from (User): Optional. For forwarded messages, sender of the original message.

        forward_from_chat (Chat): Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat.

        forward_from_message_id (int): Optional. For messages forwarded from channels, identifier of the original message in the channel.

        forward_signature (str): Optional. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present.

        forward_sender_name (str): Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages.

        forward_date (int): Optional. For forwarded messages, date the original message was sent in Unix time.

        is_topic_message (bool): Optional. True, if the message is sent to a forum topic.

        is_automatic_forward (bool): Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group.

        reply_to_message (Message): Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply..

        via_bot (User): Optional. Bot through which the message was sent.

        edit_date (int): Optional. Date the message was last edited in Unix time.

        has_protected_content (bool): Optional. True, if the message can't be forwarded.

        media_group_id (str): Optional. The unique identifier of a media message group this message belongs to.

        author_signature (str): Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator.

        text (str): Optional. For text messages, the actual UTF-8 text of the message.

        entities (list[MessageEntity]): Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.

        animation (Animation): Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set.

        audio (Audio): Optional. Message is an audio file, information about the file.

        document (Document): Optional. Message is a general file, information about the file.

        photo (list[PhotoSize]): Optional. Message is a photo, available sizes of the photo.

        sticker (Sticker): Optional. Message is a sticker, information about the sticker.

        video (Video): Optional. Message is a video, information about the video.

        video_note (VideoNote): Optional. Message is a video note, information about the video message.

        voice (Voice): Optional. Message is a voice message, information about the file.

        caption (str): Optional. Caption for the animation, audio, document, photo, video or voice.

        caption_entities (list[MessageEntity]): Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption.

        has_media_spoiler (bool): Optional. True, if the message media is covered by a spoiler animation.

        contact (Contact): Optional. Message is a shared contact, information about the contact.

        dice (Dice): Optional. Message is a dice with random value.

        game (Game): Optional. Message is a game, information about the game. More about games ».

        poll (Poll): Optional. Message is a native poll, information about the poll.

        venue (Venue): Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set.

        location (Location): Optional. Message is a shared location, information about the location.

        new_chat_members (list[User]): Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members).

        left_chat_member (User): Optional. A member was removed from the group, information about them (this member may be the bot itself).

        new_chat_title (str): Optional. A chat title was changed to this value.

        new_chat_photo (list[PhotoSize]): Optional. A chat photo was change to this value.

        delete_chat_photo (bool): Optional. Service message: the chat photo was deleted.

        group_chat_created (bool): Optional. Service message: the group has been created.

        supergroup_chat_created (bool): Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup..

        channel_chat_created (bool): Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel..

        message_auto_delete_timer_changed (MessageAutoDeleteTimerChanged): Optional. Service message: auto-delete timer settings changed in the chat.

        migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier..

        migrate_from_chat_id (int): Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier..

        pinned_message (Message): Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply..

        invoice (Invoice): Optional. Message is an invoice for a payment, information about the invoice. More about payments ».

        successful_payment (SuccessfulPayment): Optional. Message is a service message about a successful payment, information about the payment. More about payments ».

        user_shared (UserShared): Optional. Service message: a user was shared with the bot.

        chat_shared (ChatShared): Optional. Service message: a chat was shared with the bot.

        connected_website (str): Optional. The domain name of the website on which the user has logged in. More about Telegram Login ».

        write_access_allowed (WriteAccessAllowed): Optional. Service message: the user allowed the bot added to the attachment menu to write messages.

        passport_data (PassportData): Optional. Telegram Passport data.

        proximity_alert_triggered (ProximityAlertTriggered): Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location..

        forum_topic_created (ForumTopicCreated): Optional. Service message: forum topic created.

        forum_topic_edited (ForumTopicEdited): Optional. Service message: forum topic edited.

        forum_topic_closed (ForumTopicClosed): Optional. Service message: forum topic closed.

        forum_topic_reopened (ForumTopicReopened): Optional. Service message: forum topic reopened.

        general_forum_topic_hidden (GeneralForumTopicHidden): Optional. Service message: the 'General' forum topic hidden.

        general_forum_topic_unhidden (GeneralForumTopicUnhidden): Optional. Service message: the 'General' forum topic unhidden.

        video_chat_scheduled (VideoChatScheduled): Optional. Service message: video chat scheduled.

        video_chat_started (VideoChatStarted): Optional. Service message: video chat started.

        video_chat_ended (VideoChatEnded): Optional. Service message: video chat ended.

        video_chat_participants_invited (VideoChatParticipantsInvited): Optional. Service message: new participants invited to a video chat.

        web_app_data (WebAppData): Optional. Service message: data sent by a Web App.

        reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons..
    """   
    def __init__(
        self: TelegramObject,
        message_id : int = None,
        message_thread_id : int = None,
        _from : "Types.User" = None,
        sender_chat : "Types.Chat" = None,
        date : int = None,
        chat : "Types.Chat" = None,
        forward_from : "Types.User" = None,
        forward_from_chat : "Types.Chat" = None,
        forward_from_message_id : int = None,
        forward_signature : str = None,
        forward_sender_name : str = None,
        forward_date : int = None,
        is_topic_message : bool = None,
        is_automatic_forward : bool = None,
        reply_to_message : "Types.Message" = None,
        via_bot : "Types.User" = None,
        edit_date : int = None,
        has_protected_content : bool = None,
        media_group_id : str = None,
        author_signature : str = None,
        text : str = None,
        entities : list["Types.MessageEntity"] = None,
        animation : "Types.Animation" = None,
        audio : "Types.Audio" = None,
        document : "Types.Document" = None,
        photo : list["Types.PhotoSize"] = None,
        sticker : "Types.Sticker" = None,
        video : "Types.Video" = None,
        video_note : "Types.VideoNote" = None,
        voice : "Types.Voice" = None,
        caption : str = None,
        caption_entities : list["Types.MessageEntity"] = None,
        has_media_spoiler : bool = None,
        contact : "Types.Contact" = None,
        dice : "Types.Dice" = None,
        game : "Types.Game" = None,
        poll : "Types.Poll" = None,
        venue : "Types.Venue" = None,
        location : "Types.Location" = None,
        new_chat_members : list["Types.User"] = None,
        left_chat_member : "Types.User" = None,
        new_chat_title : str = None,
        new_chat_photo : list["Types.PhotoSize"] = None,
        delete_chat_photo : bool = None,
        group_chat_created : bool = None,
        supergroup_chat_created : bool = None,
        channel_chat_created : bool = None,
        message_auto_delete_timer_changed : "Types.MessageAutoDeleteTimerChanged" = None,
        migrate_to_chat_id : int = None,
        migrate_from_chat_id : int = None,
        pinned_message : "Types.Message" = None,
        invoice : "Types.Invoice" = None,
        successful_payment : "Types.SuccessfulPayment" = None,
        user_shared : "Types.UserShared" = None,
        chat_shared : "Types.ChatShared" = None,
        connected_website : str = None,
        write_access_allowed : "Types.WriteAccessAllowed" = None,
        passport_data : "Types.PassportData" = None,
        proximity_alert_triggered : "Types.ProximityAlertTriggered" = None,
        forum_topic_created : "Types.ForumTopicCreated" = None,
        forum_topic_edited : "Types.ForumTopicEdited" = None,
        forum_topic_closed : "Types.ForumTopicClosed" = None,
        forum_topic_reopened : "Types.ForumTopicReopened" = None,
        general_forum_topic_hidden : "Types.GeneralForumTopicHidden" = None,
        general_forum_topic_unhidden : "Types.GeneralForumTopicUnhidden" = None,
        video_chat_scheduled : "Types.VideoChatScheduled" = None,
        video_chat_started : "Types.VideoChatStarted" = None,
        video_chat_ended : "Types.VideoChatEnded" = None,
        video_chat_participants_invited : "Types.VideoChatParticipantsInvited" = None,
        web_app_data : "Types.WebAppData" = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
    ):
        self.update(locals())
