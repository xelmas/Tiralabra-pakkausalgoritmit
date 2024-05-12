# Toteutusdokumentti

## Yleisrakenne

Ohjelman pakkausrakenne on seuraava:
- algorithms: sisältää algoritmien lähdekoodit.
- textfiles: sisältää pakattavat teksitiedostot ja väliaikaiset tiedostot, kuten pakkaamisen yhteydessä luotu binääritiedosto ja purettu tiedosto decompressed.txt. Molemmat tiedostot poistetaan ohjelman suorituksen päätyttyä.
- tests: sisältää automaatiotestit ja yksikkötestit.
- utilities: sisältää tiedostojen käsittelijän lähdekoodin ja useamman moduulin hyödyntämät muuttujat ja apufunktiot.
- juuressa on ohjelman käyttöliittymän, toimintalogiikan ja algoritmien käsittelystä vastaavien tiedostojen lähdekoodit.
```
src/
│
├── algorithms/
│   ├── huffman.py
│   └── lzw.py
│
├── textfiles/
│   ├── sample.txt
│   ├── sample.bin 
│   └── sample_decompressed.txt
│
├── tests/
│   ├── automatic/
│   │   └── compression_comparator_automatic_test.py
│   │
│   └── unit/
│       ├── compression_comparator_test.py
│       ├── huffman_invariant_test.py
│       ├── huffman_test.py
│       ├── lzw_invariant_test.py
│       └── lzw_test.py
│
├── utils/
│   ├── filehandler.py
│   └── utils.py
│
├── main.py
├── ui.py
└── compression_comparator.py
```
## Luokkien toiminta

Ohjelman toiminta on jaettu useampaan luokkaan, joilla on oma vastuualueensa.
- `UI`: kommunikoi käyttäjän kanssa.
- `FileHandler`: suorittaa kaikki tiedostoihin liittyvät operaatiot.
- `HuffmanCoding`: toteuttaa Huffman koodauksen pakkaus- ja purkualgoritmit.
- `LZW`: toteuttaa Lempel-Ziv-Welchin pakkaus- ja purkualgoritmit.
- `CompressionComparator`: suorittaa pakkaamisen/purkamisen ja vertailee algoritmien suorituskykyä keskenään.

Ohjelman toimintalogiikka toteutetaan main-tiedostossa.

## Huffman koodaus

Omin sanoin selitettynä Huffman koodaus on luotu alla olevien pseudokoodien mukaisesti.

### Pakkaaminen

1. Lasketaan kirjainten frekvenssit tekstistä.
2. Luodaan jokaisesta kirjaimesta oma solmu(kirjain, frekvenssi, vasenLapsi, oikeaLapsi)
3. Lisätään solmut minimikekoon frekvenssin perusteella.
4. Niin kauan kun minimikeossa on yksi tai useampi solmu:
    - poista kaksi ensimmäistä solmua minimikeosta.
    - luo uusi solmu, jonka frekvenssi on yhdistettävien solmujen frekvenssien summa. Lisää yhdistetyt solmut uuden solmun lapsiksi.
    - Lisää uusi solmu minimikekoon.
5. Jäljelle jäänyt solmu on Huffmanin puun juuri.
6. Muodostetaan Huffmanin koodit kirjaimille:
    - Aloitetaan puun juuresta ja asetetaan koodiksi tyhjä merkkijono
    - Jos saavutaan lehteen, lisätään kirjain ja muodostettu Huffmanin koodi sanakirjaan.
    - Muuten tutkitaan puuta rekursiivisesti:
        - Jos solmulla on vasen lapsi, lisätään "0" tähän mennessä luotuun Huffmanin koodiin.
        - Jos solmulla on oikea lapsi, lisätään "1" tähän mennessä luotuun Huffmanin koodiin.
7. Koodataan teksti vastaamaan muodostettuja Huffmanin koodeja.
8. Luodaan merkkijonoesitys, johon muodostettu puu on tallennettu.


### Purkaminen

1. Luetaan bittejä tallennetusta Huffmanin puun esitysmuodosta ja luodaan Huffmanin puu uudelleen:
    - Jos bitti on 1, luetaan seuraavat 16-bittiä ja saadaan kirjain. Luodaan uusi solmu, jolla ei ole lapsia.
    - Jos bitti on 0, tutkitaan rekursiivisesti samalla logiikalla molemmat lapsisolmut, ja luodaan uusi solmu asettaen lapsisolmut sille.
2. Jäljelle jäänyt solmu on Huffmanin puun juuri.
3. Muodostetaan Huffmanin koodit kirjaimille:
    - Aloitetaan puun juuresta ja asetetaan koodiksi tyhjä merkkijono.
    - Jos saavutaan lehteen, lisätään muodostettu Huffmanin koodi ja kirjain sanakirjaan.
    - Muuten tutkitaan puuta rekursiivisesti:
        - Jos solmulla on vasen lapsi, lisätään "0" tähän mennessä luotuun Huffmanin koodiin.
        - Jos solmulla on oikea lapsi, lisätään "1" tähän mennessä luotuun Huffmanin koodiin.
4. Puretaan koodi korvaamalla Huffmanin koodit niitä vastaavalla kirjaimella.

## LZW

Algoritmit on luotu [GeeksForGeeks](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/)-sivuston pseudokoodin mukaisesti.

### Pakkaaminen

    PSEUDOCODE
     Initialize table with single character strings
     P = first input character
     WHILE not end of input stream
          C = next input character
          IF P + C is in the string table
            P = P + C
          ELSE
            output the code for P
          add P + C to the string table
           P = C
         END WHILE
    output code for P


### Purkaminen

    PSEUDOCODE
    Initialize table with single character strings
    OLD = first input code
    output translation of OLD
    WHILE not end of input stream
        NEW = next input code
        IF NEW is not in the string table
               S = translation of OLD
               S = S + C
       ELSE
              S = translation of NEW
       output S
       C = first character of S
       OLD + C to the string table
       OLD = NEW
    END WHILE

## Saavutetut aika- ja tilavaativuudet

### Huffman

Huffman koodauksen aikavaativuus on O(n log n), missä n on uniikkien merkkien lukumäärä. Huffmanin puun rakentamisessa poistetaan kaksi ensimmäistä alkiota minimikeosta ja yhdistetään ne luomalla uusi solmu, jonka frekvenssinä on näiden poistettujen alkioiden frekvenssien summa, ja lopuksi lisätään uusi solmu kekoon. Kun uusi solmu lisätään minimikekoon, sen aikavaativuus on O(log n). Alkioita yhdistetään n-1 kertaa yhteensä, joten kokonaisuudessaan aikavaativuudeksi saadaan O(n log n).

Tilavaativuus on O(n), missä n on uniikkien merkkien lukumäärä.

### LZW

LZW-algoritmi käy läpi tekstisyötteen kirjain kerrallaan, joten kokonaisaikavaativuus on O(n), missä n on tekstin pituus.
Algoritmin loopissa tapahtuvat sanakirja-operaatiot ovat aikavaativuudeltaan vakioita O(1), joten ne eivät vaikuta kokonaisaikavaativuuteen.

Tilavaativuus on O(n), missä n on tekstin pituus.

## Parannusehdotukset

Käyttöliittymän voisi olla graafinen. Lisäksi taulukkoon voisi lisätä kokonaisajan, mikä algoritmilla kuluu suorittaa sekä pakkaaminen että purkaminen. Tällä hetkellä taulukossa on molemmat ajat eroteltuna. 

Vertaisarvioijalta tuli hyvä ehdotus, että olisi mielenkiintoista verrata miten algoritmit suoriutuvat, kun tekstistä tiedetään jonkinlainen toisteisuuden arvo. Kokeilin tätä arvoa laskea Shannonin entropian avulla, ja se antoi ihan mielenkiintoisia tuloksia, mutta tätä ajatusta voisi kehittää lisää. Myös algoritmeja voisi kokeilla vielä paljon isommilla tiedostoilla, koska tällä hetkellä suurin testattava on noin 3 MB. 

Lisäksi voisi lisätä mahdollisuuden käyttäjälle konfiguroida algoritmien parametrejä. Esimerkiksi LZW-algoritmin yhteydessä olisi mahdollisuus vaikuttaa sanakirjan alustukseen, jolloin voisi testata suorituskykyä eri tavoin alustettujen sanakirjojen välillä. LZW-algoritmin optimointi on myös yksi mahdollinen kehitysehdotus. Tämä tarkoittaa sitä, että LZW-algoritmin sanakirja optimoidaan niin, että käyttämättömät merkit/sekvenssit välillä tyhjennetään. Tällä saadaan mahdollisesti suorituskykyä parannettua ja tallennettavan tietueen kokoa pienennettyä.

## Kielimallien käyttö

Projektissa on hyödynnetty chatGPT 3.5 ilmaisversiota suunnittelussa ja dokumentaation kielioppitarkistuksessa. Suunnitteluvaiheessa tekoälyä on hyödynnetty siten, että kysymyksen asettelu on tyyppiä "Ajattelin tehdä asian x tavalla y, mutta voisiko tapa z olla myös toimiva, mitkä ovat plussat ja miinukset näillä tavoilla?". Esimerkiksi ohjelman yleisrakenteen suunnittelussa tästä oli jonkin verran hyötyä.

Koska käytetyt algoritmit eivät olleet minulle entuudestaan tuttuja, pyysin myös tekoälyä selittämään tarkasti mitä missäkin vaiheessa pseudokoodia tehdään ja miksi, jotta ymmärsin paremmin algoritmien toimintaa. Tämä ei tosin ollut riittävän kattavasti selitetty ja oikeastaan mm. Youtubesta löytyvät opetusvideot aiheista olivat parempia oppimismielessä.

Projektin alkuvaiheessa hyödynsin myös tekoälyä tarkistamaan jotkin lauseet doctsringeistä, joiden kieliopin oikeellisuutta epäilin. Projektin edetessä en kokenut tälle enää tarvetta, sillä selkeästi tietynlainen rutiini tähän kehittyi ja usko omaan osaamiseen ilmeisesti kasvoi. Tämä oli ehkä suurin tekoälyn tuottama hyöty tässä projektissa, muutoin siitä ei ollut kauheasti hyötyä.

## Viitteet

Huffman-koodaus
- [GeeksForGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/time-and-space-complexity-of-huffman-coding-algorithm/)
- [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

Lempel-Ziv-Welch
- [Wikipedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [GeeksForGeeks](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/)
