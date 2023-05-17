from .utils import *
from Types.InlineQueryResult import InlineQueryResult

class answerWebAppQuery:
    async def answer_web_app_query(
        self,
        web_app_query_id : str = None,
        result : InlineQueryResult = None,
    ):
        """
        Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned.

        Args:
            web_app_query_id (str): Unique identifier for the query to be answered.

            result (InlineQueryResult): A JSON-serialized object describing the message to be sent.
        """

        return await Curl.request(
            url=api + "answerWebAppQuery",
            json={
                "web_app_query_id": web_app_query_id,
                "result": result,
            }
        )
