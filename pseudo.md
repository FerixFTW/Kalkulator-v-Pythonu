```python
Zacni program

input = uporabniski vnos

if ( input vsebuje '(' ):
  if( stevilo '(' in stevilo ')' ni enako ):
    vrni error in zakljuci racunanje

  poracunaj vsebino oklepajev
  rezultat vstavi nazaj v izraz
  odstrani oklepaje

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
  if( element je znak za koren ):
    rezultat = element koreni
  if( element je znak za potenciranje ):
    rezultat = element potenciraj z eksponentom na desni strani znaka za potenciranje
  if( element je ans ):
    rezultat = element ima vrednost shranjenega rezultata prejsnjega racuna

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
