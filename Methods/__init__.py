from .getUpdates import getUpdates
from .setWebhook import setWebhook
from .deleteWebhook import deleteWebhook
from .getWebhookInfo import getWebhookInfo
from .logOut import logOut
from .close import close
from .sendMessage import sendMessage
from .forwardMessage import forwardMessage
from .copyMessage import copyMessage
from .sendPhoto import sendPhoto
from .sendAudio import sendAudio
from .sendDocument import sendDocument
from .sendVideo import sendVideo
from .sendAnimation import sendAnimation
from .sendVoice import sendVoice
from .sendMediaGroup import sendMediaGroup
from .sendLocation import sendLocation
from .sendVenue import sendVenue
from .sendContact import sendContact
from .sendPoll import sendPoll
from .sendDice import sendDice
from .sendChatAction import sendChatAction
from .getUserProfilePhotos import getUserProfilePhotos
from .getFile import getFile
from .banChatMember import banChatMember
from .unbanChatMember import unbanChatMember
from .restrictChatMember import restrictChatMember
from .promoteChatMember import promoteChatMember
from .setChatAdministratorCustomTitle import setChatAdministratorCustomTitle
from .banChatSenderChat import banChatSenderChat
from .unbanChatSenderChat import unbanChatSenderChat
from .setChatPermissions import setChatPermissions
from .exportChatInviteLink import exportChatInviteLink
from .createChatInviteLink import createChatInviteLink
from .editChatInviteLink import editChatInviteLink
from .revokeChatInviteLink import revokeChatInviteLink
from .approveChatJoinRequest import approveChatJoinRequest
from .declineChatJoinRequest import declineChatJoinRequest
from .setChatPhoto import setChatPhoto
from .deleteChatPhoto import deleteChatPhoto
from .setChatTitle import setChatTitle
from .setChatDescription import setChatDescription
from .pinChatMessage import pinChatMessage
from .unpinChatMessage import unpinChatMessage
from .unpinAllChatMessages import unpinAllChatMessages
from .leaveChat import leaveChat
from .getChat import getChat
from .getChatAdministrators import getChatAdministrators
from .getChatMemberCount import getChatMemberCount
from .getChatMember import getChatMember
from .setChatStickerSet import setChatStickerSet
from .deleteChatStickerSet import deleteChatStickerSet
from .getForumTopicIconStickers import getForumTopicIconStickers
from .createForumTopic import createForumTopic
from .editForumTopic import editForumTopic
from .closeForumTopic import closeForumTopic
from .reopenForumTopic import reopenForumTopic
from .deleteForumTopic import deleteForumTopic
from .unpinAllForumTopicMessages import unpinAllForumTopicMessages
from .editGeneralForumTopic import editGeneralForumTopic
from .closeGeneralForumTopic import closeGeneralForumTopic
from .reopenGeneralForumTopic import reopenGeneralForumTopic
from .hideGeneralForumTopic import hideGeneralForumTopic
from .unhideGeneralForumTopic import unhideGeneralForumTopic
from .answerCallbackQuery import answerCallbackQuery
from .setMyCommands import setMyCommands
from .deleteMyCommands import deleteMyCommands
from .getMyCommands import getMyCommands
from .setMyName import setMyName
from .getMyName import getMyName
from .setMyDescription import setMyDescription
from .getMyDescription import getMyDescription
from .setMyShortDescription import setMyShortDescription
from .getMyShortDescription import getMyShortDescription
from .setChatMenuButton import setChatMenuButton
from .getChatMenuButton import getChatMenuButton
from .setMyDefaultAdministratorRights import setMyDefaultAdministratorRights
from .getMyDefaultAdministratorRights import getMyDefaultAdministratorRights
from .editMessageText import editMessageText
from .editMessageCaption import editMessageCaption
from .editMessageMedia import editMessageMedia
from .editMessageLiveLocation import editMessageLiveLocation
from .stopMessageLiveLocation import stopMessageLiveLocation
from .editMessageReplyMarkup import editMessageReplyMarkup
from .stopPoll import stopPoll
from .deleteMessage import deleteMessage
from .sendSticker import sendSticker
from .getStickerSet import getStickerSet
from .getCustomEmojiStickers import getCustomEmojiStickers
from .uploadStickerFile import uploadStickerFile
from .createNewStickerSet import createNewStickerSet
from .addStickerToSet import addStickerToSet
from .setStickerPositionInSet import setStickerPositionInSet
from .deleteStickerFromSet import deleteStickerFromSet
from .setStickerEmojiList import setStickerEmojiList
from .setStickerKeywords import setStickerKeywords
from .setStickerMaskPosition import setStickerMaskPosition
from .setStickerSetTitle import setStickerSetTitle
from .setStickerSetThumbnail import setStickerSetThumbnail
from .setCustomEmojiStickerSetThumbnail import setCustomEmojiStickerSetThumbnail
from .deleteStickerSet import deleteStickerSet
from .answerInlineQuery import answerInlineQuery
from .answerWebAppQuery import answerWebAppQuery
from .sendInvoice import sendInvoice
from .createInvoiceLink import createInvoiceLink
from .sendGame import sendGame
from .setGameScore import setGameScore
from .getGameHighScores import getGameHighScores


class Methods(
	getUpdates,
	setWebhook,
	deleteWebhook,
	getWebhookInfo,
	logOut,
	close,
	sendMessage,
	forwardMessage,
	copyMessage,
	sendPhoto,
	sendAudio,
	sendDocument,
	sendVideo,
	sendAnimation,
	sendVoice,
	sendMediaGroup,
	sendLocation,
	sendVenue,
	sendContact,
	sendPoll,
	sendDice,
	sendChatAction,
	getUserProfilePhotos,
	getFile,
	banChatMember,
	unbanChatMember,
	restrictChatMember,
	promoteChatMember,
	setChatAdministratorCustomTitle,
	banChatSenderChat,
	unbanChatSenderChat,
	setChatPermissions,
	exportChatInviteLink,
	createChatInviteLink,
	editChatInviteLink,
	revokeChatInviteLink,
	approveChatJoinRequest,
	declineChatJoinRequest,
	setChatPhoto,
	deleteChatPhoto,
	setChatTitle,
	setChatDescription,
	pinChatMessage,
	unpinChatMessage,
	unpinAllChatMessages,
	leaveChat,
	getChat,
	getChatAdministrators,
	getChatMemberCount,
	getChatMember,
	setChatStickerSet,
	deleteChatStickerSet,
	getForumTopicIconStickers,
	createForumTopic,
	editForumTopic,
	closeForumTopic,
	reopenForumTopic,
	deleteForumTopic,
	unpinAllForumTopicMessages,
	editGeneralForumTopic,
	closeGeneralForumTopic,
	reopenGeneralForumTopic,
	hideGeneralForumTopic,
	unhideGeneralForumTopic,
	answerCallbackQuery,
	setMyCommands,
	deleteMyCommands,
	getMyCommands,
	setMyName,
	getMyName,
	setMyDescription,
	getMyDescription,
	setMyShortDescription,
	getMyShortDescription,
	setChatMenuButton,
	getChatMenuButton,
	setMyDefaultAdministratorRights,
	getMyDefaultAdministratorRights,
	editMessageText,
	editMessageCaption,
	editMessageMedia,
	editMessageLiveLocation,
	stopMessageLiveLocation,
	editMessageReplyMarkup,
	stopPoll,
	deleteMessage,
	sendSticker,
	getStickerSet,
	getCustomEmojiStickers,
	uploadStickerFile,
	createNewStickerSet,
	addStickerToSet,
	setStickerPositionInSet,
	deleteStickerFromSet,
	setStickerEmojiList,
	setStickerKeywords,
	setStickerMaskPosition,
	setStickerSetTitle,
	setStickerSetThumbnail,
	setCustomEmojiStickerSetThumbnail,
	deleteStickerSet,
	answerInlineQuery,
	answerWebAppQuery,
	sendInvoice,
	createInvoiceLink,
	sendGame,
	setGameScore,
	getGameHighScores,): pass