# TylerBot

A trivial errbot plugin that is quick with some memes, and can issue docker commands:
  - docker run
  - docker ps
  - docker log
  - docker kill

You can also:
  - spiderman
  - batman
  - friendface

You may even get tidbits from Twitter later that say things like:
> I would cry myself to sleep but the Linux ACPI module doesn't support that on my hardware.

### Version
0.0.1

### Tech

TylerBot uses a number of open source projects to work properly:

* [errbot] - HTML enhanced for web apps!

### Todos

 - Write Tests
 - Be able to define container registry
 
License
----

MIT

# Development

To get started, you must first have python3 and pip3.

Install errbot:

```
pip3 install errbot
```

Install provider(s):

```
pip3 install "errbot[slack]"
```

Init your bot, configure, and run it. To see an example of a configuration, see:
https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

```
errbot --init
vim config.py
errbot
```

Check your output for any signs of issues, at this step, the bot should log in, and be online in the room you configured.

**Resources**

http://errbot.io/en/latest/index.html

# Usage

Direct message your bot the following to activate the plugin:

```
!plugin activate Tyler
```

After this, issue the !tyler command:

```
!tyler
```

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [errbot]: <https://github.com/errbotio/errbot>
