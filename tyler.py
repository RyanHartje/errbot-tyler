import subprocess
from errbot import BotPlugin, botcmd
from random import randint
import container


class Tyler(BotPlugin):
    """
    A bot named Tyler... or Ryan... or whatever nickname you prefer really.
      It does things, like manage docker containers locally, and give you the gift of gifs
    """

    @botcmd
    def docker(self, msg, args):

        if args == "create":
            """
            $ docker run -d --name container_name container_name
            This will run a container in detach mode if the user says:
                !tyler create container <name> [repo]
            """
            container_name = args
            new_container = container.Container(name=container_name)
            return "{0} running as ID {1}".format(container_name, new_container.id)

        elif args == "ps":
            for c in container.ps():
                yield "{0} - {1}".format(c['Image'], c['Status'])

        elif "log" in args.split()[0]:
            return "Its big its bad its wood"

    @botcmd  # flags a command
    def tyler(self, msg, args):
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        spidey = [
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
            "http://memesvault.com/wp-content/uploads/Batman-Spiderman-Memes-1.png",
            "http://67.media.tumblr.com/585c574479d92758fbb91288b6cfa562/tumblr_nushe1rL0i1s8zeifo1_400.jpg",
            "http://i3.kym-cdn.com/photos/images/original/000/168/066/superheroes-batman-superman-he-really-needs-a-driving-course.jpg",

        ]

        batty = [
            "http://memesvault.com/wp-content/uploads/2015/09/Batman-Cartoon-Memes-1.gif",
            "http://cdn.idigitaltimes.com/sites/idigitaltimes.com/files/styles/embedded_full/public/2014/08/28/2014/07/22/20339.png",
            "https://s-media-cache-ak0.pinimg.com/736x/24/5a/e1/245ae17922e87954167a22bb77addf89.jpg",
            "http://myfunnymemes.com/wp-content/uploads/2015/04/Batman-Studies-Some-Counterfeit-Money-In-The-Classic-Cartoon.jpg",
            "http://i2.kym-cdn.com/photos/images/newsfeed/001/072/255/2b1.gif",
            "https://i.gr-assets.com/images/S/photo.goodreads.com/hostedimages/1420879874i/13285083.jpg",
            "http://i3.kym-cdn.com/photos/images/original/000/483/967/273.gif",
            "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT5DffvpXusrzu0XUWFL0cpf3F1WEX1NVIBMefG2dW07IGVCT6Rn037JQ",
            "http://i0.kym-cdn.com/photos/images/original/000/220/014/Batman2.jpg",
        ]
        all_pic = batty + spidey

        if args:
            if args == 'batman':
                return batty[randint(0, len(batty) - 1)]
            elif args == 'spiderman':
                return spidey[randint(0,len(batty)-1)]
            elif args == 'snap':
                return all_pic[randint(0,len(all_pic)-1)]

        return all_pic[randint(0,len(all_pic)-1)]

    @botcmd
    def ansible(self, msg, args):
        """
        Runs an ansible command.
        Since ansible doesn't support Python3, we have to Yolo up some Subprocess calls.
        :param msg: the body of the incoming message
        :param args: the content of the arguments to ansible
        :return: the stdout for the command itself
        """
        cmd = "ansible {}".format(args)
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE
                                )
        out, _ = proc.communicate()
        return out