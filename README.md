# Valkyria

Valkyria is a robotics project "software", like the "Persocom" manga and animated "Chobits".
The base and foundation of Valkyria are 3 more or less known projects in the field of home automation: [S.A.R.A.H.][sarah] JP ENCAUSSE (fr), [GLADYS][gladys] (fr / en) and [JASPER][jasper] (en). Valkyria is developing a raspberry (raspbian *Wheezy* to migrate towards "raspbian *Jessie*").

---
### Languages
Valkyria currently uses three languages:
 - [Python][py] ([2.7][py2.7]) (interface for Prolog)
 - [NodeJS][node] ([4.X][node4]) (Human–computer interaction)
 - [Prolog][prolog] (Base rules and facts)

On the long term Python will not be part of Valkyria, which will be entirely written in NodeJS and Prolog (or equivalent) will remain the basis for rules/facts

---
### Version
0.1.0

Valkyria course is open source with a [public repository] [val] on GitHub.

---
### Installation

WARNING ! : Valkyria is currently available only a single language FRENCH. Think translate her answers!
##### Prerequisites (Raspbian / Debian)

---
##### The sound
adjust the sound output:
- in HDMI
- in Jack

the [alsa-utils][pack] package (already installed on Raspbian) provide tools to [configure][alsa] the sound output.

---
##### creation of the "TTS engine" (Text to Speech):

Valkyria uses a command (bash script) "speak".

This command is provided in the "*./bin/*" folder, it requires two commands: "*aplay*" the alsa-utils package, which reads a .wav file and "*ico2wave*" that transforms the text into .wav file

To install "*pico2wave*" on Rpi, here is an excellent[tutorial][tts]

For debian [package][libpico] "libttspico-utils" is available in the depot "non-free"


---
#### get the sources:

To retrieve the source type:
```sh
$ git clone https://github.com/RootKitDev/Valkyria NouveauDossier
```
Once the sources on your machine, test the command "speak" (ATTENTION command "pico2wave" is set to the text FRENCH Think pico adapted to your language via pico2wave man.):
```sh
$ ./bin/speak  "Voice synthesis test"
```
---
### use

If your Rpi talking, you can launch the application:
```sh
$ Cd ~ / NouveauDossier
$ Node valkyria.js
```
If when launching the application errors related to dependencies / modules happens is, run
```sh
$ Cd NouveauDossier
$ Npm install
```
"nmp install": No arguments from the root directory ("NouveauDossier" where package.json is) will install the dependencies of the application

To interact with Valkyria log on to its web interface: http: // IP_RPi: 8080 you can now Chat with Valkyria.

Valkyria do not know much yet: she knows just the "jean parents" whose links are written in Prolog via ./lib/arbre.pl, so you can ask Valkyria "who is the father of Jean "(or mother) (no accent at the moment and without"? "as well). This file is the database file rules / facts which served for testing. If you know Prolog, enjoy and change or add rules and facts

Later I hope to be able to afford a Valkyria "learn" from itself, modify these files, creating new files, etc.

---
#### contribution

Want to contribute? Great !

Send me your ideas and comments by email rootkit.dev@gmail.com.

Thank you to formulate your messages (ideas) with the following constraints:

     The title must include the following elements "Valkyria" "ModuleName" "Author"
     The body must include:
         operation "general" module
         a list (not exhaustive) module (optional for non-developers, for developers recommended)

"Author" serviera me to quote contributors, in a file, so thanked for their efforts

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


