from .utils import *
from Types.BotCommandScope import BotCommandScope

class getMyCommands:
    async def get_my_commands(
        self,
        scope : BotCommandScope = None,
        language_code : str = None,
    ):
        """
        Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned.

        Args:
            scope (BotCommandScope): A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault..

            language_code (str): A two-letter ISO 639-1 language code or an empty string.
        """

        return await Curl.request(
            url=api + "getMyCommands",
            json={
                "scope": scope,
                "language_code": language_code,
            }
        )
