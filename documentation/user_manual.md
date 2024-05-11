# Käyttöohje

## Asennusohjeet
1. Varmista, että poetry on asennettu komennolla ```poetry --version```
2. Kloonaa repositorio komennolla ```git clone```
3. Siirry hakemistoon ja asenna riippuvuudet komennolla ```poetry install```

## Käynnistysohjeet 

### Käynnistää sovelluksen interaktiivisen käyttöliittymän:
```
poetry run invoke start --function start
```

### Käynnistää sovelluksen ja ajaa pakkaus- ja purkualgoritmin kaikille tiedostoille automaattisesti
```
poetry run invoke start --function automatic_start
```

## Testien ajaminen

### Suorittaa yksikkötestit:
```
poetry run invoke unit-tests
```

### Suorittaa automaattitestit:
Automaattitestit suorittavat testit kaikille tekstitiedostoille, joten tämä vie noin 25 sekuntia.
```
poetry run invoke automatic-tests
```

### Suorittaa kaikki testit:
Suorittaa sekä automaatti- että yksikkötestit, joten tämä vie noin 30 sekuntia.
```
poetry run invoke test
```

### Luo testikattavuusraportin kaikille testeille:
Suorittaa sekä automaatti- että yksittötestit ja luo raportin, joten tämä vie noin 70 sekuntia.
```
poetry run invoke coverage-report
```

# Sovelluksen käyttö

## Interaktiivinen käyttöliittymä

Kun käyttäjä käynnistää sovelluksen, terminaaliin tulostuu allaolevan mukainen taulukko, jossa on listattuna kaikki ei-tyhjät tekstitiedostot. Käyttäjää pyydetään valitsemaan tiedosto pakattavaksi syöttämällä sitä vastaava numero taulukon ensimmäisestä sarakkeesta.

![tiedoston valinta](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/choose_file.png)

Kun tiedosto on valittu, käyttäjälle tulostetaan valitun tiedoston nimi ja seuraavaksi pyydetään valitsemaan millä algoritmilla tiedosto pakataan vai käytetäänkö molempia. 

![algoritmin valinta](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/choose_algorithm.png)

Vaihtoehdot ovat:
- H: käytetään Huffman koodaus -algoritmia.
- L: käytetään LZW-algoritmia.
- C: käytetään molempia algoritmeja.
- E: poistutaan valikosta.

### Yksittäisen algoritmin valinta

Mikäli käyttäjä valitsee vaihtoehdon "H" tai "L", pyydetän käyttäjää valitsemaan toiminto.
Vaihtoehdot ovat:
- C: pakataan tiedosto valitulla algoritmilla.
- D: puretaan tiedosto valitulla algoritmilla.
- E: poistutaan valikosta.

Esimerkkitapauksessamme käyttäjä valitsee ensin algoritmiksi "H", eli Huffman koodauksen. Tämän jälkeen käyttäjä valitsee "C", eli tiedosto pakataan. Sovellus suorittaa pakkaamisen ja tulostaa statistiikat käyttäjälle konsoliin.

![pakkaaminen](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/compressing_example.png)

Koska purkamista ei ole vielä suoritettu, on taulukossa "Decompression time"-sarakkeessa arvona 0.0000. Seuraavaksi, kun käyttäjä valitsee "D", pakattu tiedosto puretaan, ja taulukon riville päivitetään purkamiseen kulunut aika oikeaan sarakkeeseen.

![purkaminen](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/decompressing_example.png)

Huomiona tässä, että käyttäjä ei voi valita purkamista "D" ennen kuin tiedosto on pakattu toiminnolla "C". Sovellus ilmoittaa, mikäli käyttäjä yrittää purkaa tiedoston ennen sen pakkaamista. 

Ohjelman suoritus päättyy, kun käyttäjä poistuu päävalikosta komennolla "E".

### Molempien algoritmien valinta

Mikäli käyttäjä valitsee vaihtoehdon "C", ajetaan molemmille algoritmeille pakkaus- ja purkutoiminnot. Tulokset päivitetään taulukkoon ja tulostetaa lopuksi käyttäjälle konsoliin. Ohjelman suoritus päättyy.

![vertailu](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/compare_example.png)

## Automaattinen ajo (ei interaktiivinen käyttöliittymä)

Kun sovellus käynnistetään komennolla automatic_start, sovelluksessa ei ole interaktiivista käyttöliittymää. Sovellus ajaa pakkaus- ja purkutoiminnot kaikille ei-tyhjille tiedostoille ja tallentaa statistiikat taulukkoon. Lopuksi taulukko tulostetaan käyttäjälle nähtäväksi konsoliin.

![vertailu](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/automatic_example.png)

