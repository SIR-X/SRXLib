from .utils import *
import typing


class deleteMessage:
    async def delete_message(
        self,
        chat_id : typing.Union[int, str] = None,
        message_id : int = None,
    ):
        """
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.
        
        The following methods and objects allow your bot to handle stickers and sticker sets.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Identifier of the message to delete.
        """

        return await Curl.request(
            url=self.api + "deleteMessage",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )
