# Valkyria

Valkyria est un projet de robotique "logiciel", à l'image des "Persocom" du manga et animé "Chobits".
Les base et fondements de Valkyria sont 3 projets plus ou moins connu dans le domaine de la domotique :  [S.A.R.A.H.][sarah] de JP ENCAUSSE (fr), [GLADYS][gladys] (fr/en) et [JASPER][jasper] (en). Valkyria est développer sur un raspberry (raspbian *Wheezy* migrer vers "raspbian *Jessie*").

### Langages utilisés
Valkyria utilise actuellement trois langages:
 - [Python][py] ([2.7][py2.7]) (Interface pour Prolog)
 - [NodeJS][node] ([4.X][node4]) (Interface Homme-Machine)
 - [Prolog][prolog] (Base de règles et de faits)

Sur le long terme Python ne fera plus partie de Valkyria, qui sera écrite entierement en NodeJS et Prolog (ou équivalent) restera pour la base de règles/faits

### Version
0.1.0

Bien sûr Valkyria est open source avec un [dépôt public][val] sur GitHub.

### Installation

ATTENTION ! :
Valkyria n'est actuellement disponible qu'une une seul langage le FRANCAIS. Pense à traduire ses réponses!

##### Pré-requis (raspbian / Debian)
##### Le son
---
régler la sorti son :
 - en HDMI
 - en Jack

le package [alsa-utils][pack] (déja installé sur raspbian) fournir les outils pour [configurer][alsa] la sorti son.

##### création du "moteur tts"(Text to Speech):
---
Valkyria utilise une commande (script bash)  : "speak".

Cette commande est fournie dans le dossier "*./bin/*", elle necéssite deux autres commandes : "*aplay*" du package alsa-ulits, qui lit un fichier .wav et "*pico2wave*" qui transforme du texte en fichier .wav

Pour installer "*pico2wave*" sur Rpi voici un excellent [tutoriel][tts]

Pour debian le [package][libpico] "*libttspico-utils*" est disponible dans les depot "non-free"

#### récupérer les sources :
---
Pour récupérer les source tapez :
```sh
$ git clone https://github.com/RootKitDev/Valkyria NouveauDossier
```
Une fois les sources sur votre machine, testez la commande "speak" (ATTENTION la commande "*pico2wave*" est réglée pour du texte en FRANCAIS. Pense a adapté pico a votre langue via ```man pico2wave```) :
```sh
$ cd NouveauDossier/bin
$ ./speak "test de synthese vocal" 
```
### Utilisation
Si votre Rpi parle, vous pouvez lancer l'application:
```sh
$ cd ~/NouveauDossier
$ node valkyria.js
```
Si lors du lancement de l'application une erreur lié aux dépendences/modules se produit, executez
```sh
$ cd NouveauDossier
$ npm install
```
"nmp install" : Sans arguments et depuis le répertoire racine ("NouveauDossier" là où se trouve package.json) va installer les dépendances de l'application

Pour interagir avec Valkyria connectez-vous sur son interface web : http://IP_RPi:8080
vous pouvez à présent tchatez avec Valkyria.

Valkyria ne sait pas grand-chose pour le moment :
elle connait juste les "parents de jean", dont les liens sont écris via Prolog dans ``./lib/arbre.pl``,
vous pouvez donc demander a Valkyria "qui est le pere de jean" (ou la mere) (sans accent pour le moment et sans "?" également). Ce fichier est le fichier de base de règles/faits qui a servie pour les tests. Si vous connaissez Prolog, profitez en et changez les ou ajoutez des règles et faits

Plus tard j'espere permettre a Valkyria de pouvoir "apprendre" d'elle-même, en modifier ces fichiers, en créant de nouveaux fichier, etc 
 
### Contribution

Vous voulez contribuer? Très bien !

Envoyez-moi vos idées et commentaires par mail <rootkit.dev@gmail.com>.

Merci de formulez vos mails (d'idées) selon les contraintes suivants:

 - Le titre doit comporter les éléments suivants *"Valkyria" "ModuleName" "Author"*
 - Le corps doit comprendre :
    -  le fonctionnement "général" du module
    -  une liste (non exhaustive) des modules (*optionel pour les non-développeurs , recommandé pour les développeurs*)

"Author" me serviera à citer les contributeurs, dans un fichier, afin de les remerciés pour leurs efforts

License
----

MIT


**Free Software, Hell Yeah!**

[//]:

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
