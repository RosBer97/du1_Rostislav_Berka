# zadani ukolu viz: https://github.com/xtompok/uvod-do-prg_19/blob/master/du1/zadani.md
# osetreno: vstup jiny nez A, M, L, B ; meritko rovno nebo mensi 0 (funguje pouze pri vstupu integer),
# osetreno: zaporny polomer zeme (funguje pouze pri vstupu integer), mercator pro 90°, cisla vetsi nez 1 m
# osetreno: zelvi kresleni– hodnoty >= 100 nekresli, poledniky u mercatora nad 80° protahne,
#pokud jsou všechny poledniky nebo rovnobezky v seznamu nad 100 cm, zelva nenakresli vůbec nic
# (jen kvůli rovníku a poledníku 0° by to nemělo smysl)
## ve volitelnem vstupu osetrena prilis mala/velka sirka/delka, mercator pro 90°, a vystup >= 100 cm

pass
from math import tan, log, e, radians, sin
from turtle import forward, backward, exitonclick, left, right, penup, pendown, speed, shape
import turtle
pass


#definovani rovnobezek (pokud by byl pozadavek na jiny interval nez 10°, muze se hodit)
#vystupem je seznam rovnobezek (rov) po 10° od 10 do 90°.
def rovnobez():
    rovnobez = []
    rov = 0
    while rov != 90:
        rov = rov + 10
        rovnobez.append(rov)
    return rovnobez
rov = rovnobez()

#definovani poledniku (pokud by byl pozadavek na jiny interval nez 10°, muze se hodit)
#vystupem je seznam poledniku (pol) po 10° od 10° do 180°.
def polednik():
    polednik = []
    pol = 0
    while pol != 180:
        pol = pol + 10
        polednik.append(pol)
    return polednik
pol = polednik()

####################################### vstupy od uzivatele (zobrazeni, meritko, polomer):    ###################
#vstup od uzivatele-zobrazeni(CRS)
#uzivatele zada sour. system pomoci danych pismen. V pripade ze zada neco jineho nez 4 definovana zobrazeni
#program ho nepusti dal. Vystupem je jedno ze 4 pismen pro zobrazeni.
def vstup_zobr():
    crs = ""
    while crs != "L" or "A" or "B" or "M":
        crs = input("Zvolte zobrazení (L, A, B nebo M:)")
        if crs == "L":
            break
        elif crs == "A":
            break
        elif crs == "B":
            break
        elif crs == "M":
            break
        else:
            print("Neplatný vstup, zadejte L, A, B nebo M!")
    return crs


#vstup od uzivatele-meritko
#uzivatel zada meritko x ve formatu 1 : x. Osetreno je meritko <= 0. Vystupem je promena meritko.
def vstup_mer():
    mer = 0
    while mer <= 0:
        mer = int(input("Zadejte prosím celočíselné měřítko:"))
        if mer > int(0):
            break
        else:
            print("Měřítko musí být větší než nula!")
    return mer


#vstup od uzivatele-polomer zeme
#uzivatel zada polomer zeme, pokud zada cislo mensi nez 0, SW ho dal nepusti, pri zadani 0 je polomer 6371.11 km. vystupem je polomer zeme.
def polomer_zeme():
    polomer = 0
    while float(polomer) <= float(0):
        polomer = float(input("Zadejte poloměr Země v km, 0 znamená 6371,11 km:"))
        if polomer == 0:
           polomer = 6371.11
           break
        elif polomer > 0:
            break
        else:
            print("zadejte kladné číslo (poloměr v km) nebo 0 (6371,11 km)")
    return polomer

#nacteni vyse uvedenych vstupu od uzivatele do promennych a prevedeni meritka na cm se kteryma se po celou dobu
# bude pracovat:
sour_system = vstup_zobr()
meritko = vstup_mer()
polomer_km = polomer_zeme()
#polomer v cm
polomer_cm = polomer_km * 100000

################################# konec vstupů od uzivatele (zobrazeni, meritko, polomer):   ###################

#definovani vzorcu pro vypocet poledniku (stejne pro vsechna 4 zobr.) a pro jednotliva zobrazeni.
#vstupem je vzdyz konkretni rovnobezka v ° (pripadne polednik), zadane meritko a polomer v cm.
#vystupem je vypocitana vzdalenost na papire pro danou rovnobezku (polednik)

#poledniky definovani vypoctu
def vzorec_polednik(poled_zem, meritko, polomer):
    return round((radians(poled_zem)) * polomer/meritko,1)

#lambert definovani vypoctu
def vzorec_lam(rovno_zem, meritko, polomer):
    return round((sin(radians(rovno_zem))) * polomer/meritko,1)

#braun definovani vypoctu
def vzorec_braun(rovno_zem, meritko, polomer):
    return round((tan((radians(rovno_zem))/2)) * 2 * polomer/meritko,1)

#marin definovani vypoctu
def vzorec_mar(rovno_zem, meritko, polomer):
    return round((radians(rovno_zem)) * polomer/meritko,1)

#mercator definovani vypoctu
def vzorec_mer(rovno_zem, meritko, polomer):
    return round((log(1/tan(radians((90-rovno_zem)/2)))) * polomer/meritko,1)

#vypocet poledniku
#samotny vypocet celeho seznamu poledniku s while cyklem. vstupem je seznam poledniku ve ° (pol),
#meritko v cm a zadany polomer. vystupem je seznam s vypocitanymi vzdalenostmi na papire ---->
#chybi vsak 0 a zaporne hodnoty
def vypocet_pol(poledniky, meritko, polomer):
    poled_zem = 0
    poled_papir = 0
    sez_final = []
    while len(poledniky) != 0:
        poled_zem = poledniky.pop()
        poled_papir = vzorec_polednik(poled_zem, meritko, polomer)
        sez_final.append(poled_papir)
    return sez_final

#vypocet rovnobezek
#vstupy jsou obdobne jako u poledniku, akorat sem vstupuje seznam rovnobezek (rov),
#dale je vstupem pismeno definujici sour. system. vystupem je seznam se vzdalenosmi na papire
#bez 0 a zapornych hodnot. Musel byt osetren vstup pro mercatora - viz nize.
def vypocet_zobr(rovnobezky, meritko, polomer, crs):
    rovno_zem = 0
    rovno_papir = 0
    sez_final = []
    while len(rovnobezky) != 0:
        rovno_zem = rovnobezky.pop()
        if crs == "B":
            rovno_papir = vzorec_braun(rovno_zem, meritko, polomer)
        if crs == "L":
            rovno_papir = vzorec_lam(rovno_zem, meritko, polomer)
        if crs == "M":
            if rovno_zem == 90:
                continue ######### mercator neexistuje pro 90°, 90° tak bylo zahozeno
            else:
                rovno_papir = vzorec_mer(rovno_zem, meritko, polomer)
        if crs == "A":
            rovno_papir = vzorec_mar(rovno_zem, meritko, polomer)
        if crs == "M" and rovno_zem == 90: ####### pri mercatorovi a zem. sirce 90°  nic neprirazovat do seznamu
            pass
        else:
            sez_final.append(rovno_papir)
    return sez_final

#zkoumani zda nejsou hodnoty vetsi nez 100, kdyz hodnota >= 100, pak napise "-"
#fce, ktera zajistuje aby v seznamu nebyly hodnoty vetsi nez 100 cm. vstupem je seznam z fce pridam_zaporna
#ktery jiz obsahuje i zaporne hodnoty a 0. Vystupem je seznam kdy misto hodnot > 100 jsou pouze "-".
def moc_velke(seznam):
    sez_pomlcka = []
    while seznam:
        hodnota = seznam.pop()
        if -100 < hodnota < 100:
            sez_pomlcka.append(hodnota)
        else:
            sez_pomlcka.append("-")
    return sez_pomlcka

# zkomletovani seznamů pro koncového uzivatele (pridani zapornych hodnot a nuly)
#funkce jejiz ukolem je pridat do vypocteneho seznamu 0 a zaporne hodnoty. vstupem jsou seznamy z fci
#vypocet_zobr a vypocet_pol, ktere jeste neobsahuji zaporne hodnoty a 0. Vystupem je seznmam
#rovnobezek (resp. poledniku) jenz je urcen k zobrazeni koncovemu uzivateli.
def pridam_zaporna(sez_vstupni):
    sez_kladny = sez_vstupni[:]
    sez_zaporny = []
    hodnota_zaporna = 0
    while sez_vstupni:
        hodnota_zaporna = sez_vstupni.pop() * (-1)
        sez_zaporny.append(hodnota_zaporna)
    sez_komplet = sez_zaporny + sez_kladny
    sez_komplet.append(0)
    sez_komplet.sort(reverse = True)
    sez_print = moc_velke(sez_komplet)   ### nahrazeni prilis velkych hodnot pomlckou
    return sez_print

# jiz jen formality, prirazeni seznamu s kladnymi rovnobezkami (poledniky) vypocitanymi funkcemi (vypocet_zobr a vypocet_pol)
# vznikl predpoklad ze seznam pouze s kladnymi hodnotami bez 0 by se mohl hodit pri zelvim kresleni.
poledniky_kladne = vypocet_pol(pol, meritko, polomer_cm)
rovno_kladne = vypocet_zobr(rov, meritko, polomer_cm, sour_system)
#nakopirovani seznamu poledniku a rovnobezek pro zelvu. v dalsim kroku totiz sezamy poledniky_kladne a rovno_kladne vyprazdnin fci pop,
## do zelvy bych potom posilal prazdne seznamy...
pol_zelva = poledniky_kladne[:]
rov_zelva = rovno_kladne[:]
#prirazeni seznamu se vsemi hodnotami i zapornymi + 0. Uceno k zobrazeni koncovemu uzivateli.
rov_for_user = pridam_zaporna(rovno_kladne)
pol_for_user = pridam_zaporna(poledniky_kladne)
#vypsani finalnich vysledku uzivateli.
print("Rovnobezky:", rov_for_user)
print("Poledniky", pol_for_user)

################################################    ZELVI KRESLENI    ############################################
shape("turtle")  ## <-- aby byla zelva krasavice

#pokud je hodnota >= 100, tak je vymazana, aby ji zelva nekreslila (obdobne jako ve vypisu
#pro uzivatele maji byt pomlcky misto techto hodnot)

def mensi_nez_100(seznam):
    sez_bez100 = []
    while seznam:
        hodnota = seznam.pop()
        if hodnota < 100:
            sez_bez100.append(hodnota * 10) #aby želva vykreslovala v mm musím vynasobit * 10
        else:
            continue
    return sez_bez100

#nacteni seznamu bez hodnot vetsich nebo rovno 100 vstupujiciho do zelvy do promennych
pol_bez100 = mensi_nez_100(pol_zelva)
rov_bez100 = mensi_nez_100(rov_zelva)


#####   pokud je bud seznam poledniku nebo rovnobezek prazdny (vsechny hodnoty poledniku nebo
#### rovnobezek jsou vetsi nez 1 m), zelva nenakresli nic, proto podminka if
####  kazdy ze seznamu musi obsahovat aspon 1 hodnotu:
if pol_bez100 and rov_bez100:

    print("zelva nakresli poledniky v techto vzdalenostech od pocatku souradnic (pix resp. mm) na obe strany:", pol_bez100)
    print("zelva nakresli rovnobezky v techto vzdalenostech od pocatku souradnic (pix resp. mm) na obe strany:", rov_bez100)

    # delka poledniku = dvojnasobna delka vzdalenosti 90° rovnobezky

    if sour_system == "M":    ### Mercator jde do nekonecna, aby to bylo naznaceno u delky poledniku
                            ### pridavam k delce poledniku jeste 20 % nejvzdalenejsi rovnobezky, coz by mohla byt docela rozumna hodnota
        pol_delka = (max(rov_bez100) * 2) + (max(rov_bez100)*1/5)
        print("zelvi kresleni – delka kreslenych poledniku (pix resp. mm):",pol_delka)
    else:
        pol_delka = max(rov_bez100) * 2
        print("zelvi kresleni – delka kreslenych poledniku (pix resp. mm):",pol_delka)


    #delka rovnobezek = dvojnasobna delka vzdalenosti 180° poledniku
    rov_delka = max(pol_bez100) * 2
    print("zelvi kresleni – delka kreslenych rovnobezek (pix resp. mm):",rov_delka)

    ################ ZDE ZACINA ZELVA KRESLIT  #####################

    turtle.speed(0)
    turtle.pensize(1.5)

    #zelva kresli celou sit smerem dolů... Aby mela dostatek prostoru a co nejvice ho vyuzila, tak ji
    #na zacatku posunu o 350 pixelu nahoru. Pak se zda byt tak akorat. Testovano na 4K a FullHD monitorech,
    # pri roztazeni okna s zelvi grafikou na celou obrazovku s mercatorem, meritkem 1: 50 000 000 a r = 6371.11.
    # pri tomto nastaveni se cela sit krasne vejde na monitor.
    penup()
    left(90)
    forward(350)
    left(180)
    pendown()
    #nakreslí nultý poledník alias greenwich
    forward(pol_delka)
    backward(pol_delka)
    right(90)

    turtle.pensize(1)

    ### funkce na kresleni poledniku i rovnobezek. Je rozdelena na dve casti, pouzije se podle toho ktera polokoule se zrovna kresli
    ## vstupem je vzdalenost od pocatecni cary (rovnik nebo greenwich), delka poledniku nebo rovnobezky a cislo charakterizujici polokouli
    def jedna_cara(vzdalenost, delka, polokoule):
        if polokoule == 0:
            penup()
            forward(vzdalenost)
            left(90)
            pendown()
            forward(delka)
            backward(delka)
            left(90)
            penup()
            forward(vzdalenost)
            pendown()
        if polokoule == 1:   ##### to same jako vyse, ale zelva se otaci na druhou stranu, kresli
                                ### druhou polokouli
            penup()
            forward(vzdalenost)
            right(90)
            pendown()
            forward(delka)
            backward(delka)
            right(90)
            penup()
            forward(vzdalenost)
            pendown()

    #####kresli poledniky nastridacku. nejdriv na zapadni polokouli, pak na vychodni. Stale se opakuje az nakresli posledni polednik
    ### (vycerpa seznam poledniku)
    while pol_bez100:
        vzdalenost = pol_bez100.pop()
        jedna_cara(vzdalenost, pol_delka, 0)
        jedna_cara(vzdalenost, pol_delka, 1)

    ##########################################  presunuti na kresleni rovnobezek ###################
    # zacina kreslit opet od rovniku

    penup()
    forward(rov_delka/2)
    left(90)
    forward(pol_delka/2)
    pendown()

    #nakresli rovnik
    turtle.pensize(1.5)
    left(90)
    forward(rov_delka)
    backward(rov_delka)
    right(90)
    turtle.pensize(1)

    #nakresli rovnobezky, opet nastridacku, stejny system jako u poledniku

    while rov_bez100:
        vzdalenost = rov_bez100.pop()
        jedna_cara(vzdalenost, rov_delka, 0)
        jedna_cara(vzdalenost, rov_delka, 1)

    exitonclick()
else:   #####  zelva nekresli, jestlize je jeden ze seznamu prazdny, viz pocatecni podminka nahore.
    print("Vzdalenosti rovnobezek nebo poledniku od pocatku souradnic byly vetsi nez 1 m. Zelva je smutna, nema co kreslit.")
    pass


############################################### VYPOCET VOLITELNEHO BODU   ######################
# vyber zobrazeni
def vypocet_volitelny_bod(rovnobezka, meritko, polomer, crs):
    if crs == "B":
        rovno_papir = vzorec_braun(rovnobezka, meritko, polomer)
    if crs == "L":
        rovno_papir = vzorec_lam(rovnobezka, meritko, polomer)
    if crs == "M":
        rovno_papir = vzorec_mer(rovnobezka, meritko, polomer)
    if crs == "A":
        rovno_papir = vzorec_mar(rovnobezka, meritko, polomer)
    return rovno_papir
## cyklus zajistujici chod programu a neustale tazani se
sirka = 5.5
delka = 5.5
while sirka != 0 and delka != 0:
    sirka = float(input("Zadejte zemepisnou sirku napr. ve tvaru 45.26"))
    delka = float(input("Zadejte zemepisnou delku napr. ve tvaru 14.87"))
    if (-90 > sirka or 90 < sirka) or (-180 > delka or 180 < delka):
        print("Neplatná zem. sirka a/nebo delka! zadejte sirku v intervalu <-90;90> a delku v intervalu <-180;180>")
        continue
    elif sirka == 0 and delka == 0:
        print("Dekuji za pouziti programu.")
        break
    elif sour_system == "M" and (sirka == -90 or sirka == 90):
        print("Mercatorovo zobrazeni neexistuje pro -90°a 90° zadejte jinou zem. sirku!")
        continue
    else:
        x_papir = float()
        y_papir = float()
        y_papir = vypocet_volitelny_bod(sirka, meritko, polomer_cm, sour_system)
        x_papir = vzorec_polednik(delka, meritko, polomer_cm)
        if x_papir <= -100 or x_papir >= 100:
            x_papir = "-"
        if y_papir <= -100 or y_papir >= 100:
            y_papir = "-"
    print("Zem. delka (X na papire):", x_papir, "Zem. sirka (Y na papire):", y_papir)