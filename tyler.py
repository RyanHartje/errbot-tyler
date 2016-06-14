from errbot import BotPlugin, botcmd
from random import randint


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
        gifs = [
                "https://media.giphy.com/media/xTiTnHvXHHxOTcdmxO/giphy.gif",
                "https://media.giphy.com/media/yoJC2HuqslbIL96pna/giphy.gif",
                "https://media.giphy.com/media/EVSvdu4pGF8DS/giphy.gif",
                "https://media.giphy.com/media/mVunxEOvj6YPm/giphy.gif",
                "https://media.giphy.com/media/9Di5AeO06hgmk/giphy.gif"
                "http://unrealitymag.com/wp-content/uploads/2011/05/spider-man14.jpg",
                "http://i0.kym-cdn.com/photos/images/original/000/114/109/tumblr_ljntiuWDlD1qar3nbo1_500.jpg",
                "http://www.spiderfan.org/shows/images/spiderman_tv_1960s/s01e15/screen01.jpg",
                "https://thepwnzone.files.wordpress.com/2011/07/spiderman-meme-generator-hold-a-sec-how-do-i-shoot-web-efcd21.jpg",
                "https://thepwnzone.files.wordpress.com/2011/07/original.jpg",
                "https://s-media-cache-ak0.pinimg.com/736x/b5/49/00/b549003a8959412e94e5e5981b61dfc8.jpg",
                "http://cdn.smosh.com/sites/default/files/bloguploads/60s-spiderman-meme-babies.jpg",
                "https://s-media-cache-ak0.pinimg.com/236x/a9/e8/1a/a9e81a8ebb36a747f0aef39fae182ede.jpg",
                "http://i.imgur.com/uorRV.jpg",
                "http://i2.kym-cdn.com/photos/images/newsfeed/000/110/831/1301181202460.jpg",
                "http://i3.kym-cdn.com/photos/images/original/000/121/757/barrel.jpg",
                "https://s-media-cache-ak0.pinimg.com/236x/ae/0e/ea/ae0eea2fc834359d813cf8b974482ab3.jpg",
                "http://i1.kym-cdn.com/photos/images/facebook/000/110/272/tumblr_litkzaldnn1qghlk1o1_500.jpg",
                "http://memesvault.com/wp-content/uploads/Spiderman-Meme-Desk-Like-A-Boss-9.jpg",
                "http://themetapicture.com/media/funny-Spider-Man-cartoon-villain-mustaches-behind.jpg",

               ]
 
        return gifs[randint(0,len(gifs)-1)]

