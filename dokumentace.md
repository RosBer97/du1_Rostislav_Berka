# Domácí úkol 1 - zobrazení

## Zadání
Úkolem bylo napsat program, který spočítá souřadnice rovnoběžek a poledníků,
tak aby bylo možno nakreslit souřadnicovou síť pro dané zobrazení.
Zadáno bylo Marinovo, Lambertovo, Braunovo a Mercatorovo zobrazení. 
Podrobné zadání je dostupné na odkaze: https://bit.ly/33e43NR
### Vstup
Uživatel si vybere zobrazení pomocí zadání jednoho z písmen: 
- `L` - Lambertovo zobrazení
- `A` - Marinovo zobrazení 
- `B` - Braunovo zobrazení 
- `M` - Mercatorovo zobrazení 

Dále zadá číslo `x`, které bude odpovídat měřítku 1:x, například pokud zadá 50000000, 
bude se počítat s měřítkem 1:50 000 000. Také je možno navolit poloměr Země, při 
zadání čísla 0 se počítá s 6371,11 km.
### Výstup
Výstupem je seznam rovnoběžek a poledníků po 10° pro obě polokoule. Následně také
program nakreslí souřadnicovou síť pro dané zobrazení s pomocí želví grafiky. Pro
informativní účely také vypíše souřadnice rovnoběžek a poledníků v pixelech 
respektive v mm a délku poledníků i rovnoběžek, s pomocí kterých želva kreslí síť.
Pokud je nějaká hodnota větší nebo rovna 100 cm, program vypíše místo ní pomlčku a 
želva hodnotu nenakreslí. Nakonec si uživatel může nechat spočítat souřadnice zvoleného bodu. 
Při zadání souřadnic 0, 0 program skončí. Zvolený bod je počítán v zobrazení, které již bylo 
použito pro výpočet celé sítě. Totéž se týká měřítka a poloměru Země. 
## Funkcionalita programu
### Základní funkčnost
Program začíná vygenerováním rovnoběžek a poledníků po 10° <0°;90°>. Následují 3 dotazy na vstupy 
od uživatele – zobrazení, měřítko, poloměr Země. Tyto hodnoty jsou uloženy do proměnných.
Poloměr je ještě převeden na cm. Následuje vytvoření funkcí se vzorci pro výpočet jednotlivých zobrazení
a pro výpočet poledníků. Následují funkce vypocet_pol a vypocet_zobr, ve kterých jsou vypočítány celé seznamy 
vzdáleností od počátku souřadnic s pomocí definovaných vzorců v předešlém kroku. 
Výstupem jsou seznamy poledniky_kladne a rovno_kladne, které obsahují pouze kladné hodnoty,
což se hodí v želví grafice. Nicméně pro uživatele jsou ve funkci pridam_zaporna přidány 
záporná čísla a 0, přičemž ve funkci moc_velke jsou nahrazeny hodnoty větší nebo rovny
100 cm pomlčkou.
### Želví grafika
Na začátku jsou seznamy s kladnými hodnotami. Z těch jsou ve funkci mensi_nez_100
odstraněny hodnoty >= 100. S tím souvisí problém, pokud by byly všechny hodnoty >= 100
želva by neměla co kreslit. Proto je zde podmínka if, která zaručuje spuštění programu jen
v případě, že oba seznamy obsahují aspoň 1 hodnotu. Program tedy nenakreslí ani rovník, či nultý 
poledník, což se zdálo zbytečné při neexistenci jiné rovnoběžky nebo poledníku. 
Následují informativní výstupy pro uživatele obsahující co bude želva kreslit – délky,
vzdálenosti atd. Jsou totiž vypočítány délky poledníků a rovnoběžek, následně je želva posunuta
o 350 pixelů nahoru na startovní pozici, jelikož želva jinak kreslí celou síť směrem dolů. 
Potřebuje tedy prostor. Následně je definována funkce jedna_cara, která nakreslí jednu 
čáru (poledník/rovnoběžku) a vrátí želvu na začátek. Funkce obsahuje verzi zvlášť pro každou polokouli.
Následně je vytvořena síť poledníků, která s pomocí while cyklu kreslí nastřídačku obě
polokoule. Poté se želva přesune a následuje totéž pro poledníky. 
### Volitelný vstup uživatele
Nejprve je definována funkce, která posílá hodnoty do správného vzorce
pro zobrazení (podle toho jaké si uživatel na začátku vybral). Následuje while cyklus,
který zajišťuje chod této celé funkce. Nejprve se zeptá na vstupy. Následně vyhodnotí 
správnost vstupu (viz nekorektní vstupy níže). Pokud jsou vstupy v pořádku, pošle
hodnoty do vzorců pro výpočet poledníků a rovnoběžek. Poté vyhodnocuje,
jeslti náhodou nejsou hodnoty >= 100. Pokud ano, vypisuje pomlčku. Program
vypíše výsledky uživateli a díky while cyklu se celý stále opakuje, dokud 
uživatel nezadá bod 0, 0.
### Nekorektní vstupy
V programu jsou ošetřeny následující nekorektní vstupy a situace:
- Vstup jiný než A, M, L, B
- Měřítko <= 0 (funguje při vstupu integer)
- záporný poloměr Země (funguje při vstupu integer)
- Mercátorovo zobrazení při 90°
- Pomlčky místo čísel větších než 1 m 

U želví grafiky je ošetřeno:
- Nekreslí hodnoty >= 100 cm
- Mírně protáhne poledníky u Mercatorova zobrazení tak, aby bylo jasné, že jde do nekonečna

U volitelného bodu:
- Mercator pro -90°a 90°
- Příliš malá/velká zem. šířka/délka (např. zem. šířka 150° neexistuje)
- Při hodnotách >= 100 cm vypíše pomlčky místo čísel


