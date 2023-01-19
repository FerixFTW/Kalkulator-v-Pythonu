```python
Zacni program

input = uporabniski vnos

if( input je pot do datoteke ):
  for( vrstica v datoteki ):
    input = vrstica
    program(input)

### Ugotovi kaj se bo racunalo

zacasni_array = pretvori input v array, loci po presledkih
pretvorbe = ["BIN","OCT","HEX","DEC"]
logicne = ["AND","OR","NOT","NOR","NAND","XOR","XNOR"]

### Izvedi logicne operacije
if zacasni_array dolgi vsaj 4:
  if prvi element zacasni_array med pretvorbe in ali tretji ali cetrti element zacasni_array med logicne:
    sistem = prvi element zacasni_array
    zanikan_prvi = True ce se pred prvo cifro nahaja "NOT"
    zanikan_drugi = True ce se pred drugo cifro nahaja "NOT"
    prva_cifra = prva cifra v izrazu
    druga_cifra = druga cifra v izrazu
    operator = zeljena operacija

    parsed_array[sistem]

    if zanikan_prvi:
      negiraj(prva_cifra) in parsed_array.dodaj(prva_cifra)
    else:
      parsed_array.dodaj(prva_cifra)
    if zanikan_drugi:
      negiraj(druga_cifra) in parsed_array.dodaj(druga_cifra)
    else:
      parsed_array.dodaj(druga_cifra)

    vrni in izpisi rezultat resi_logicno(parsed_array)

### Izvedi pretvorbo sistemov
if zacasni_array dolgi 3 in vsebuje na začetku in tretjem mestu element iz pretvorbe:
  vir = prvi element zacasni_array
  cifra = drugi element zacasni_array
  cilj = tretji element zacasni_array

  vrni in izpisi rezultat VIRtoCILJ(cifra)

if ( input vsebuje '(' ):
  if( stevilo '(' in stevilo ')' ni enako ):
    vrni error in zakljuci racunanje

  poracunaj vsebino oklepajev
  rezultat vstavi nazaj v izraz
  odstrani oklepaje

  poenostavljen izraz podaj naprej v računanje

### Izvedi klasicno racunanje

array = []
operatorji = ['+','-','*','/']

for( vsak znak v inputu ):
  if( znak v operatorji ):
      cifra = vsi znaki do operatorja
      array.dodaj(cifra)
      array.dodaj(operator)

for( vsak element v arrayu ):
  if( element prazen ):
    array.odstrani(element)

for( vsak element v arrayu ):
  if( element je ans ):
    rezultat = element ima vrednost shranjenega rezultata prejsnjega racuna
  if( element je znak za koren ali 'q' ):
    rezultat = element koreni
  if( element je znak za potenciranje ):
    rezultat = element potenciraj z eksponentom na desni strani znaka za potenciranje

  element zamenjaj z rezultatom

for( vsak element v arrayu ):
  if( element je '%'):
    rezultat = element je ostanek pri deljenju levega in desnega števila
  if( element je '*' ):
    rezultat = element je produkt levega in desnega števila
  if( element je '/' ):
    rezultat = element je kvocient levega in desnega števila

  element zamenjaj z rezultatom

for( vsak element v arrayu ):
  if( element je znak za seštevanje ):
    rezultat = seštej cifri na levi in desni od operatorja
  if( element je znak za odštevanje ):
    rezultat = razlika med ciframa na levi in desni od operatorja

    element zamenjaj z rezultatom
    odstrani operator in desno cifro iz arraya

rezultat = prvi element arraya

izpisi rezultat

Konec programa
```
