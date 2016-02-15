__author__ = 'Florian Kibler'

import csv, sys


class Converter(object):
    pfad = ""

    def __init__(self, pfad):
        self.pfad = pfad
        dialekt = self.sniffer(self.pfad)
        print(dialekt)
        # Der Dialekt eines CSV-Files wird ueberprueft und das File wird in der Konsole ausgegeben
        self.lesen()
        print("Speicherung in ein neues File " + pfad + "NEU.csv")
        # Ein neues CSV File mit validen Header wird erstellt
        self.schreiben()
        # Ein Csv File wird kopiert und extra Content wird angehaengt
        self.newfile()
        print("Speicherung in ein neues File " + pfad + "NEW.csv")

    """
        Diese Klasse enthaelt Methoden um ein CSV-File:
            - einzulesen und auszugeben
            - Ein neues Csv File zu erstellen und in dieses etwas hinein zu speichern
    """

    def schreiben(self):
        # Das File wird geoeffnet
        with open(self.pfad + 'NEU.csv', 'w') as csvfile:
            fieldnames = ['T', 'WV', 'WK', 'BZ', 'SPR', 'WBER', 'ABG', 'UNG', 'SPOE',
                          'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'T': '1', 'WV': '1', 'WK': '0', 'BZ': '0', 'SPR': '0', 'WBER': '1234556', 'ABG': '366656',
                             'UNG': '23459',
                             'SPOE': '236663', 'FPOE': '5751', 'OEVP': '56789', 'GRUE': '345666', 'NEOS': '346567',
                             'WWW': '3409', 'ANDAS': '3467', 'GFW': '7765', 'SLP': '2', 'WIFF': '136', 'M': '12',
                             'FREIE': '7'})

    """
        Diese Methode schreibt den Inhalt eines Files in ein anderes, sprich das File wird kopiert.
        Ausserdem kann extra Content an das File gefuegt werden
    """

    def newfile(self):
        # Ausgangsdaten
        ifile = open(self.pfad + '.csv', "r")
        reader = csv.reader(ifile)
        # Exportfile
        ofile = open(self.pfad + 'NEW.csv', "w")
        writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        # Zuerst werden die alten Daten in das File drangehaengt
        for row in reader:
            writer.writerow(row)
        # Danach wird der writer neu konfiguriert und extra Content wird in das File geschrieben
        fieldnames = ['T', 'WV', 'WK', 'BZ', 'SPR', 'WBER', 'ABG', 'UNG', 'SPOE',
                      'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE']
        writer = csv.DictWriter(ofile, fieldnames=fieldnames)

        writer.writerow(
            {'T': '1', 'WV': '1', 'WK': '0', 'BZ': '0', 'SPR': '0', 'WBER': '1234556', 'ABG': '366656', 'UNG': '23459',
             'SPOE': '236663', 'FPOE': '5751', 'OEVP': '56789', 'GRUE': '345666', 'NEOS': '346567',
             'WWW': '3409', 'ANDAS': '3467', 'GFW': '7765', 'SLP': '2', 'WIFF': '136', 'M': '12', 'FREIE': '7'})

        ifile.close()
        ofile.close()

    """
    Diese Methode ist dazu dar um ein CSV-File zu lesen und in der Konsole auszugeben
    Es ist wichtig, dass alle verschiedenen Dialekte ausgegeben werden koennen
    Dialekte: ['unix', 'excel-tab', 'excel']
    Ich habe die Methode mit allen  verschiedenen Dialekten getestet und alle konnten gleichermassen ausgelesen werden
    """

    def lesen(self):
        filename = self.pfad + '.csv'
        out = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f, self.sniffer(filename))
                try:
                    for row in reader:
                        print(row)
                        out.append(row)
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            return out
        except FileNotFoundError as er:
            return 'Datei existiert nicht!'


"""
    Diese Methode ermittelt den Dialekt anhand der Trennzeichen und gibt diesen dann zurueck
"""


def sniffer(self, filename):
    # Alle moeglichen Trennzeichen verpacke ich in eine Liste
    moegliche_Trennzeichen = [',', ';', '\t', ' ', '|', ':']
    try:
        # Es wird ueberprueft ob eines der oben angefuehrten Trennzeichen vorhanden ist
        dialect = csv.Sniffer().sniff(filename + '.csv', moegliche_Trennzeichen)
    except:
        # Wenn nicht gibt es keinen Dialekt
        dialect = None
    return dialect


if __name__ == '__main__':
    test = Converter("csv")

"""
import csv, codecs

class Converter:
    def __init__(self, filename):
        self.inhalt=None
        f = open(filename, 'r')
        self.reader = csv.reader(f, dialect=csv.excel)

    def opencsv(self):
        self.inhalt = ''
        for row in self.reader:
            self.inhalt+=row

    def recognize(self):
        sn = csv.Sniffer()
        s = sn.sniff(self.opencsv())
        return s.delimiter



c = Converter('csv.txt')
c.opencsv()
print(c.inhalt)
"""
