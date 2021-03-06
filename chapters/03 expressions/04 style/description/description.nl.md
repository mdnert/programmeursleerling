Misschien is het je opgevallen dat ik in mijn voorbeelden veel spaties
gebruik. Bijvoorbeeld, bij de haakjes die achter een functienaam staan,
zet ik altijd een spatie na het openingshaakje en voor het sluithaakje.
In berekeningen zet ik vaak spaties rondom operatoren als dat de
berekening beter leesbaar maakt. Ik zet ook vaak lege regels in mijn
code, en gebruik consequent vier spaties als tabulatie waar nodig.

De meeste van deze zaken zijn gewoon "stijl." De spaties bij de haakjes
en rond de operatoren zijn niet nodig. Python begrijpt de code ook prima
als ze er niet staan. De volgende vier regels code zijn equivalent:

```python
# Equivalente regels code
print( 2 + 3 )
print(2+3)
print( 2+3)
print       (       2       +       3       )
```

Het "vastplakken" van het openingshaakje aan de functienaam doet vrijwel
iedere programmeur, maar de rest verschillen de stijlen van spaties
plaatsen tussen programmeurs (bijvoorbeeld, mijn stijl waarin ik een
spatie plaats voor een sluithaakje is hoogst zeldzaam). Je kunt hierin
je eigen stijlvoorkeur gebruiken, je hoeft niet de mijne te volgen. Maar
ik raad je wel aan om een consistente stijl te gebruiken, want dat maakt
je code leesbaarder, zelfs voor programmeurs die er een andere stijl op
nahouden.

Merk op dat de code hierboven een "hash mark" (\#; hiervoor bestaat geen
Nederlandstalig woord) heeft op de eerste regel, waarna een tekst volgt
die wat details over de code uitlegt. Deze regel is een commentaarregel:
als je een hash mark gebruikt in je code (behalve als die in een string
staat, natuurlijk) dan is alles wat rechts van de hash mark staat op de
regel commentaar, dat door Python genegeerd wordt. Je kunt commentaar
gebruiken om details over je code te geven, als je denkt dat uitleg
nodig is. Meer over het geven van commentaar volgt in een later
hoofdstuk.
