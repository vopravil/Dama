Dáma
Klasická hra dáma pro dva hráče, AI opponent in progress
Plně funkční desková hra Dáma naprogramovaná v Pythonu s využitím knihovny Pygame. Projekt využívá vlastní objektově orientované třídy pro reprezentaci herní desky a validaci tahů.

Pravidla a herní mechaniky

Hra pro dva hráče: Hraje se lokálně na jednom zařízení, hráči se plynule střídají v tazích.
Povinné braní: Hra automaticky hlídá platné tahy. Pokud má hráč možnost přeskočit (sebrat) soupeřovu figurku, tento tah je vynucený a nelze táhnout jinam.
Skákání dozadu: Oproti klasickým pravidlům je v této verzi hry povoleno přeskakovat soupeřovy figurky i směrem dozadu.
Vícenásobné skoky: Pokud po sebrání figurky navazuje další možný skok, hráč v něm pokračuje (řetězení skoků).

Spuštění hry

Ujistěte se, že máte nainstalovaný Python.
Nainstalujte potřebnou knihovnu pomocí terminálu: pip install pygame
Spusťte hlavní soubor s hrou (např. python main.py).
