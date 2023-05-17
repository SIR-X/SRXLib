from .utils import *
from Types.InputFile import InputFile

class setChatPhoto:
    async def set_chat_photo(
        self,
        chat_id : int | str = None,
        photo : InputFile = None,
    ):
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            photo (InputFile): New chat photo, uploaded using multipart/form-data.
        """

        return await Curl.request(
            url=api + "setChatPhoto",
            json={
                "chat_id": chat_id,
                "photo": photo,
            }
        )
