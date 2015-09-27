var app = require('express')(),
    server = require('http').createServer(app),
    io = require('socket.io').listen(server),
    ent = require('ent'), // bloquer les caractères HTML
    exec = require('child-process-promise').exec,
    Regex = require("regex"),
    fs = require('fs');

var reqNet = false

app.get('/', function (req, res) {
    res.sendfile('./views/index.html');
});

io.sockets.on('connection', function (socket, pseudo) {

    // Dès qu'on nous donne un pseudo, on le stocke en variable de session et on informe les autres personnes
    socket.on('nouveau_client', function(pseudo) {
        pseudo = ent.encode(pseudo);
        socket.pseudo = pseudo;

        console.log(pseudo + ' vien de se connection !');
    });

    // Dès qu'on reçoit un message, on récupère le pseudo de son auteur et on le transmet aux autres personnes
    socket.on('message', function (message) {

        message = ent.encode(message);
        msgRes = message.split("'").join("\\'").split("?").join("\\?")

        console.log('Un message a été reçus');

        if (reqNet) {
            if (message == 'oui') {
                console.log('préparation de la requete');
                msgRes = '';
            }
            else if (message == 'non') {
                console.log('requete annulée');
                reqNet = false;
                msgRes = '';
            }
        }

        if (msgRes != ''){

            exec('sudo python app.py "' + msgRes + '"', function(){

                var file = fs.createReadStream('./file/rep');
                var data = '';

                file.on('data', function(chunk) {
                    data += chunk;
                });

                file.on('end', function() {
                    exec('./bin/speak "' + data + '"', function() {

                       var regex = /Internet/;
                       if (regex.test(data)){
                            console.log("En attente de confirmation de requete web");
                            reqNet = true
                       }
                    });
                });
            });
        }
    });
});

server.listen(8080);
