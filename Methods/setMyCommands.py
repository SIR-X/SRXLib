from .utils import *
from Types.BotCommandScope import BotCommandScope
from Types.BotCommand import BotCommand

class setMyCommands:
    async def set_my_commands(
        self,
        commands : list[BotCommand] = None,
        scope : BotCommandScope = None,
        language_code : str = None,
    ):
        """
        Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success.

        Args:
            commands (list[BotCommand]): A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified..

            scope (BotCommandScope): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault..

            language_code (str): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.
        """

        return await Curl.request(
            url=api + "setMyCommands",
            json={
                "commands": commands,
                "scope": scope,
                "language_code": language_code,
            }
        )
