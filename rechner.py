#Begrüßungsnachricht
print('Herzlich Willkommen beim Monopolyrechner von Zero ©!' +
     '\n' +
     'Nachfolgend werden die Scheine einzeln abgefragt (1, 5, 10, 20, 50, 100, 500).')

#Bis zur Nutzereingabe bleib die Begrüßungsnachricht bestehen
input('Um fortzufahren drücke bitte die Enter-Taste.')

#Liste der verfügbaren Scheine im Spiel
scheine = [1, 5, 10, 20, 50, 100, 500]

#Liste mit den Ergebnissen für Spieler 1
sp1 = []

#Liste mit den Ergebnissen für Spieler 2
sp2 = []

#Summe für Spieler 1
sum1 = []

#Summe für Spieler 2
sum2 = []


# Klassendefinierung Spieler 1
def spieler1():
    # Schleife um die Scheine zu Berechnen
    for items in scheine:
        # Anzahl der Scheine wird vom Nutzer eingegeben
        h=input('Scheinanzahl eingeben: ')

        # Berechnung der Geldsumme der Scheine
        items=items * int(h)

        # Liste sp1 wird um die jeweiligen Einträge erweitert
        sp1.append(items)


# Klassendefinierung Spieler 2
def spieler2():
    # Schleife um die Scheine zu Berechnen
    for items in scheine:
        # Anzahl der Scheine wird vom Nutzer eingegeben
        h=input('Scheinanzahl eingeben: ')

        # Berechnung der Geldsumme der Scheine
        items=items * int(h)

        # Liste sp1 wird um die jeweiligen Einträge erweitert
        sp2.append(items)


# Klasse spieler1 wird ausgeführt
spieler1()


# Klassendefinierung Abfrage
def abfrage():
    i=input('Berechnung für Spieler 2 Starten?'+
            ' J / N ?')

    if i=='J':

        # Klasse spieler2 wird ausgeführt
        spieler2()

        # Berechnung des Gesamtergebnisses für Spieler 1
        for l in sp1:
            l+l

        # Berechnung des Gesamtergebnisses für Spieler 2
        for k in sp2:
            k+k

        # Gewinnerermittlung
        o=l-k

        if o > 0:
            print('Spieler 1 gewinnt.')

        elif o==0:
            print('Untentschieden.')

        else:
            print('Spieler 2 gewinnt.')

        # Hält das Programm bis zu einer Nutzereingabe offen
        input('Enter zum beenden drücken.')

    elif i=='N':

        # Berechnung des Gesamtergebnisses für Spieler 1
        for l in sp1:
            l+l

        # Benachrichtigung bei keiner weiteren Berechnung
        print('Alles klar, ich schließe nun das Programm...'+
              '\n'+
              'Spieler 1 hat folgende Summe erreicht: '+
              str(l))

        # Hält das Programm bis zu einer Nutzereingabe offen
        input('Enter zum beenden drücken.')

    else:
        # Benachrichtigung über fehlerhafte Eingabe und wiederholung der Abfrage
        print('Falsche Eingabe...')
        abfrage()


# Klasse abfrage wird ausgeführt
abfrage()
