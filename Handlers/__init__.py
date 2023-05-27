from .handlers import *
from .decorators import *

class DHandlers(
    OnMessage,
    OnEditedMessage,
    OnChannelPost,
    OnEditedChannelPost,
    OnInlineQuery,
    OnChosenInlineResult,
    OnCallbackQuery,
    OnShippingQuery,
    OnPreCheckoutQuery,
    OnPoll,
    OnPollAnswer,
    OnMyChatMember,
    OnChatMember,
    OnChatJoinRequest
): pass