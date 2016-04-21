# Valkyria

Valkyria is a robotics project "software", like the "Persocom" manga and animated "Chobits".
The base and foundation of Valkyria are three more or less known projects in the field of home automation: [S.A.R.A.H.][sarah] JP ENCAUSSE (fr), [GLADYS][gladys] (fr/en) and [JASPER][jasper] (en). Valkyria is developing a raspberry Pi (raspbian *Wheezy* to migrate towards "raspbian *Jessie*").

---
### Languages
Valkyria currently uses three languages:
 - [Python][py] ([2.7][py2.7]) (interface for Prolog)
 - [NodeJS][node] ([4.X][node4]) (Human–computer interaction)
 - [Prolog][prolog] (Base rules and facts)

On the long term Python will not be part of Valkyria, which will be entirely written in NodeJS and Prolog (or equivalent) will remain the base rules/facts
toto
---
### Version
0.1.0

Valkyria course is open source with a [public repository] [val] on GitHub.

---
### Installation

WARNING ! :
Valkyria is currently available only a single language: the FRENCH. Don't forget to  translate her answers!

##### Prerequisites (Raspbian / Debian)

---
##### The sound
Set the output sound is:
- in HDMI
- in Jack

[alsa-utils][pack] package (already installed on Raspbian) provide tools to [configure][alsa] the sound output.

---
##### Creation of the "TTS engine" (Text to Speech):

Valkyria uses a command (bash script) "speak".

This command is provided in the "*./bin/*" folder, it requires two commands: "*aplay*" the alsa-utils package, which reads a .wav file and "*ico2wave*" that transforms the text into .wav file

To install "*pico2wave*" on Rpi, here is an excellent[tutorial][tts]

For debian [package][libpico] "libttspico-utils" is available in the depot "non-free"


---
#### Getting the source:

To get the source, run:
```sh
$ cd ~/
$ git clone https://github.com/RootKitDev/Valkyria NewDir
```
Once the sources on your machine, test the command "speak" (WARNING ! The command "*pico2wave*" is set to the FRENCH text. Don't forget to pico suited to your language via ```man pico2wave```):
```sh
$ cd ~/NewDir
$ ./bin/speak "voice synthesis test"
```

---
### Use:

If your Rpi talking, you can install dependencies and launch the application:
```sh
$ cd ~/NewDir
$ npm install
$ node valkyria.js
```
```nmp install```: No arguments from the root directory ("NewDir" where package.json is) will install the dependencies of the application

To interact with Valkyria log on to her web interface: "http://IP_RPi:8080" you can now Chat with Valkyria.

Valkyria don't know much yet: she knows just the "jean parents" whose links are written in ``./lib/arbre.pl`` via Prolog, so you can ask Valkyria "who is the father of Jean "(or mother) (no accent at the moment and without"? "as well). This file is the base rules/facts which served for testing. If you know Prolog, enjoy and change or add rules and facts

Later I hope to be able to allow Valkyria "learn" from herself, modify these files, creating new files, etc.

---
#### Contribution:

Want to contribute? Great !

Send me your ideas and comments by email: <rootkit.dev@gmail.com>.

Thank you to provide your email (ideas) according to the following constraints:

  - The title must include the following elements: *"Valkyria" "ModuleName" "Author"*
  - The body must include:
  	  - the general operation of the module
      - a list (not exhaustive) module (*optional for non-developers, for developers recommended*)

"Author" serve me to quote contributors, to thank them for their efforts

----
### License

MIT

**Free Software, Hell Yeah!**

---

[val]: <https://github.com/RootKitDev/Valkyria>
[git-repo-url]: <https://github.com/joemccann/dillinger.git>
[node.js]: <http://nodejs.org>
[express]: <http://expressjs.com>
[sarah]: <http://news.encausse.net/sarah/>
[gladys]: <http://gladysproject.com>
[jasper]: <https://jasperproject.github.io/>
[node4]: <https://nodejs.org/en/blog/release/v4.0.0/>
[prolog]: <http://www.swi-prolog.org/>
[py]: <https://www.python.org/>
[node]: <https://nodejs.org/en/>
[py2.7]: <https://www.python.org/downloads/>
[alsa]: <http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/>
[pack]: <https://packages.debian.org/fr/wheezy/libttspico-utils>
[tts]: <http://rpihome.blogspot.fr/2015/02/installing-pico-tts.html>
[libpico]: <https://packages.debian.org/fr/wheezy/libttspico-utils>
