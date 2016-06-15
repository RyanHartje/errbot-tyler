from errbot import BotPlugin, botcmd
import requests

class Tyler(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tyler(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        giphyAPI = 'http://api.giphy.com'
        giphyRandEnd = '/v1/gifs/random'
        giphyPubToken = 'dc6zaTOxFJmzC'

        giphyParams = dict()
        giphyParams['api_key'] = giphyPubToken
        giphyParams['gifFind'] = 'batman' 

        randomGif = requests.get(giphyAPI+giphyRandEnd, params=giphyParams)
        displayGif = randomGif.json()['data']['fixed_width_small_url']
        return displayGif

