ServizioPubblico
================

Un semplice script per scaricare le puntante da www.serviziopubblico.it

Informazioni
----------------------
Un semplice script che permette la visione dei video di Servizio Pubblico senza l'utilizzo di un browser dedicato.

Lo stream è trasmesso all'indirizzo http://www.serviziopubblico.it/


Installazione
----------------------
Per l'installazione è sufficiente eseguire:

    sudo python setup.py install

Avrete il comando `serviziopubblico` pronta per l'utilizzo:

    $ serviziopubblico -h
      Usage: serviziopubblico [options] url

      Options:
      -h, --help            show this help message and exit
      -d, --download        download video
      -p PLAYER, --player=PLAYER
                            choose video player [default: vlc]



Esempi
----------------------

Per **scaricare** una puntanta:

    serviziopubblico -d http://www.serviziopubblico.it/puntate/lo-stato-criminale/
    
Per **visualizzare** una puntanta utilizzando `mplayer`:

    serviziopubblico -p mplayer http://www.serviziopubblico.it/puntate/lo-stato-criminale/
