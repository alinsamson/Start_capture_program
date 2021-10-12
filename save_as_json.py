
class Pachet(object):
    """
    Aceasta clasa este conceputa pentru a crea un obiect  sub forma unui JSON, JSON ce ulterior va fi
    salvat intr-un fisier creat la o anumita cale.
    Args:
        Ethernet_dst, Ethernet_src, IP_src, IP_dst,IP_version, IP_proto, TCP_sport,
        TCP_dport, UDP_sport, UDP_dport - folosite pentru a retine anumite valori din pachetul creat
    Methods:
        __str__() : metoda suprascrisa ce va returna o reprezentare de tip JSON
    """
    def __init__(self, Ethernet_dst, Ethernet_src, IP_src, IP_dst,IP_version, IP_proto,
                 TCP_sport, TCP_dport, UDP_sport, UDP_dport):
        """
        Metoda constructor necesara pentru definirea atributelor ce vor captura datele din pachet.
        Args:
            Ethernet_dst : valoarea corespunzatoare pentru Ethernet_dst din pachet
            Ethernet_src : valoarea corespunzatoare pentru Ethernet_src din pachet
            IP_src       : valoarea corespunzatoare pentru IP_src din pachet
            IP_dst       : valoarea corespunzatoare pentru IP_dst din pachet
            IP_version   : valoarea corespunzatoare pentru IP_version din pachet
            IP_proto     : valoarea corespunzatoare pentru IP_proto din pachet
            TCP_sport    : valoarea corespunzatoare pentru TCP_sport din pachet
            TCP_dport    : valoarea corespunzatoare pentru TCP_dport din pachet
            UDP_sport    : valoarea corespunzatoare pentru UDP_sport din pachet
            UDP_dport    : valoarea corespunzatoare pentru UDP_dport din pachet
        """
        self.Ethernet_dst = Ethernet_dst
        self.Ethernet_src = Ethernet_src
        self.IP_dst = IP_dst
        self.IP_src = IP_src
        self.IP_version = IP_version
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UDP_sport = UDP_sport
        self.UDP_dport = UDP_dport

    def __str__(self):
        """
        Metoda suprascrisa ce este utilizata pentru a defini modul in care se vor afisa instantele
        obiectelor. Aceasta metoda este folosita pentru a afisa un format de tip JSON.
        Return:
            reprezentare_json : un format de tip JSON
        """
        reprezentare_json = {
            'Ethernet': {'src': self.Ethernet_src, 'dst': self.Ethernet_dst},
            'IP': {'src': self.IP_src, 'dst': self.IP_dst, 'version': self.IP_version, 'proto': self.IP_proto},
            'TCP': {'sport': self.TCP_sport, 'dport': self.TCP_dport},
            'UDP': {'sport': self.UDP_sport, 'dport': self.UDP_dport}
        }
        return reprezentare_json

