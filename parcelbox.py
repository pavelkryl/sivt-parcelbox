
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    # jmeno a prijmeni dohromady
    name: str
    phone: str
    email: str


@dataclass
class Parcel:
    id: str
    pin: str
    description: Optional[str]
    sender: Person
    recipient: Person


class AbstractParcelBox(ABC):

    @abstractmethod
    def hand_in(self, sender: Person, recipient: Person, description: Optional[str] = None) -> Parcel:
        '''
        Prebira zasilku/balicek od odesilatele, notifikuje jak odesilatele tak prijemce.
        :param sender: odesilatel, tomu se zasila potvrzeni
        :param recipient: prijemce, tomu se zasila vyzva k vyzvednuti
        :param description: volitelny popisek balicku
        :returns: reprezentace prevzateho balicku (s vygenerovanym id a pin)
        '''

    @abstractmethod
    def hand_out(self, id: str, pin: str) -> Optional[Parcel]:
        '''
        Vydava zasilku, notifikuje odesilatele o jejim vydani.
        :param id: id zasilky (z notifikace/vyzvy k vyzvednuti)
        :param pin: PIN k vyzvednuti
        :returns: reprezentace vydaneho balicku, nebo None v pripade ze balicek neexistuje nebo PIN nesedi
        '''

    # dobrovolne rozsireni: vydani pouze dle PINu
    #@abstractmethod
    #def vydej_zasilku_dle_pin(self, pin: str) -> Optional[Zasilka]:
        #...


# doplnte zde jeste kontrakt pro notifikator, napr. AbstractNotifier, ktery bude umet zasilat text oznameni na danou mailovou adresu
# tento notifikator bude uvnitr pouzivat vase implementace AbstractParcelBoxu