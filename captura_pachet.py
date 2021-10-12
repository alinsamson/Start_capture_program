import json
from scapy.all import *
from save_as_json import Pachet

class Capture(object):
    """
    Aceasta clasa este conceputa pentru a efectua o captura pe toate interfetele de retea.Clasa Capture
    este o clasa de tip Singleton care va asigura ca se va crea o singura instanta a unei capturi la un
    moment dat.
    Args:
        instance        : reprezinta instanta creata la un moment dat
        captura_pachete : variabila ce retine captura facute pe pachetele de retea
        nr_pachete_tcp  : variabila ce retine numarul de pachete de tip TCP
        nr_pachete_udp  : variabila ce retine numarul de pachete de tip UDP
        json_final      : lista ce va cuprinde elementele de tip json salvate

    Methods:
        __init__()      : metoda constructor
        get_instance    : metoda de clasa ce va crea o instanta
        make_captura    : metoda statica ce va genera o captura pe interfetele de retea
        save_json       : metoda statica ce va salva json-ul creat intr-un fisier
    """
    instance = None
    captura_pachete = None
    nr_pachete_tcp = 0
    nr_pachete_udp = 0
    json_final = []

    @classmethod
    def get_instance(cls):
        """
        Metoda de clasa necesara pentru design pattern-ul de tip Singleton ce va returna o instanta.
        Args:
            cls : intotdeauna primul argument al unei metode de clasa
        """
        if cls.instance == None:
            cls.instance = Capture()
        return cls.instance

    def __init__(self):
        """
        Metoda constructor ce va returna un mesaj specific pentru cazurile in care se doreste crearea
        unui numar de instante mai mare de 1. Clasa Capture fiind o clasa de tip Singleton, este strict
        necesar sa se creeze o singura instanta la un moment dat.
        """
        if Capture.instance != None:
            raise ValueError('A Singleton instance is already existing!')
        else:
            Capture.__instance = self

    @staticmethod
    def make_captura():
        """
        Metoda statica creata cu scopul de a efectua o anumita captura pe toate interfetele de retea.
        Metoda va importa din modulul Scapy functia sniff pentru a putea efectua captura. De asemeanea
        in cadrul acestei metode vom verifica tipul pachetelor din captura proaspat creata si vom
        modifica variabilele de clasa concepute cu scopul de a retine numarul de pachete TCP/UDP,
        variabile ce vor fi utilizate in momentul crearii diagramei circulare.
        Return:
            captura_pachete (list) : lista cu pachetele de retea
        """
        Capture.captura_pachete = sniff(count=5, filter='ip')
        for pachet in Capture.captura_pachete:
            if TCP in pachet:
                Capture.nr_pachete_tcp += 1
            elif UDP in pachet:
                Capture.nr_pachete_udp +=1
        Capture.get_instance()
        return Capture.captura_pachete

    @staticmethod
    def save_json(cale):
        """
        Metoda statica conceputa cu scopul de a instantia pentru fiecare pachet din captura un obiect de
        tip Pachet cu atributele specifice si de a salva reprezentarea obiectului creat sub forma de
        JSON intr-un fisier.
        Args:
            cale (str) : reprezinta calea fisierului in care se va salva JSON-ul final.
        Return:
            "cale" : un fisier ce va contine JSON-ul creat
        """
        for pachet in Capture.captura_pachete:
            if Ether in pachet:
                ether_src = pachet[Ether].src
                ether_dst = pachet[Ether].dst
            else:
                ether_dst = None
                ether_src = None

            if IP in pachet:
                ip_dst = pachet[IP].dst
                ip_src = pachet[IP].src
                ip_version = pachet[IP].version
                ip_proto = pachet[IP].proto
            else:
                ip_dst = None
                ip_src = None
                ip_proto = None
                ip_version = None

            if TCP in pachet:
                tcp_dport = pachet[TCP].dport
                tcp_sport = pachet[TCP].sport
                udp_sport = None
                udp_dport = None
            elif UDP in pachet:
                udp_sport = pachet[UDP].sport
                udp_dport = pachet[UDP].dport
                tcp_dport = None
                tcp_sport = None
            else:
                udp_sport = None
                udp_dport = None
                tcp_dport = None
                tcp_sport = None

            instanta_noua = Pachet(ether_dst, ether_src, ip_src, ip_dst, ip_version, ip_proto,
                                   tcp_sport, tcp_dport, udp_sport, udp_dport)

            pachet_nou = Pachet.__str__(instanta_noua)
            Capture.json_final.append(pachet_nou)

        with open(cale, mode = 'w') as fff:
            json.dump(Capture.json_final, fff, indent=4, separators=(",",":"))

#Nu am ales sa folosesc pentru calea in care vom salva fisierul o cale de tipul: C:\Users\Documents\Python
#Deoarece am considerat ca e mai dificil sa scriu in filtru aceasta cale. Mai usor poate fi sa ii dam un nume
#Si abia apoi se poate muta fisierul de tip json intr-un alt director
#Pentru a da o cale cu caractere speciale se foloseste de regula raw string
