from .utils import *
from Types.InlineQueryResult import InlineQueryResult
from Types.InlineQueryResultsButton import InlineQueryResultsButton

class answerInlineQuery:
    async def answer_inline_query(
        self,
        inline_query_id : str = None,
        results : list[InlineQueryResult] = None,
        cache_time : int = None,
        is_personal : bool = None,
        next_offset : str = None,
        button : InlineQueryResultsButton = None,
    ):
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        Args:
            inline_query_id (str): Unique identifier for the answered query.

            results (list[InlineQueryResult]): A JSON-serialized array of results for the inline query.

            cache_time (int): The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300..

            is_personal (bool): Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query..

            next_offset (str): Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes..

            button (InlineQueryResultsButton): A JSON-serialized object describing a button to be shown above inline query results.
        """

        return await Curl.request(
            url=api + "answerInlineQuery",
            json={
                "inline_query_id": inline_query_id,
                "results": results,
                "cache_time": cache_time,
                "is_personal": is_personal,
                "next_offset": next_offset,
                "button": button,
            }
        )
