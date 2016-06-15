import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

#BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.
BACKEND = 'Slack'
STORAGE = 'Shelf'

BOT_ASYNC = True

BOT_DATA_DIR = '/Users/ryanhartje/source/python/errbot-tyler/data'
BOT_EXTRA_PLUGIN_DIR = '/Users/ryanhartje/source/python/errbot-tyler/plugins'

BOT_LOG_FILE = '/Users/ryanhartje/source/python/errbot-tyler/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@ryan', '@ryantoo', '@tyler' )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!
BOT_IDENTITY = {
    'server': ('chatterbots.slack.com',5222),
    'token': 'xoxb-50964359203-4cDrWR8XtXtpzbUUaHfSzYqQ',
}

CHATROOM_PRESENCE = ('general',)
BOT_PREFIX = '!'
