from .utils import *
from Types.BotCommandScope import BotCommandScope

class deleteMyCommands:
    async def delete_my_commands(
        self,
        scope : BotCommandScope = None,
        language_code : str = None,
    ):
        """
        Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.

        Args:
            scope (BotCommandScope): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault..

            language_code (str): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.
        """

        return await Curl.request(
            url=api + "deleteMyCommands",
            json={
                "scope": scope,
                "language_code": language_code,
            }
        )
