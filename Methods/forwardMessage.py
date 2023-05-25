from .utils import *
import typing


class forwardMessage:
    async def forward_message(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        from_chat_id : typing.Union[int, str] = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        message_id : int = None,
    ):
        """
        Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            from_chat_id (int | str): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the forwarded message from forwarding and saving.

            message_id (int): Message identifier in the chat specified in from_chat_id.
        """

        return await Curl.request(
            url=self.api + "forwardMessage",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "from_chat_id": from_chat_id,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "message_id": message_id,
            }
        )
