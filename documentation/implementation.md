# Toteutusdokumentti

## Yleisrakenne

Ohjelman rakenne on seuraava:
- algorithms-kansio: sisältää algoritmien lähdekoodit.
- textfiles-kansio: sisältää pakattavat teksitiedostot ja väliaikaiset tiedostot, kuten pakkaamisen yhteydessä luotu binääritiedosto ja purettu tiedosto decompressed.txt. Molemmat tiedostot poistetaan ohjelman suorituksen päätyttyä.
- utilities-kansio: sisältää tiedostojen käsittelijän lähdekoodin ja useamman moduulin hyödyntämät muuttujat ja apufunktiot.

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
│   ├── huffman_invariant_test.py
│   ├── huffman_test.py
│   ├── lzw_invariant_test.py
│   ├── lzw_test.py
│
├── utils/
│   ├── filehandler.py
│   └── utils.py
│
├── main.py
├── ui.py
└── compression_comparator.py

## Luokkien toiminta

Ohjelman toiminta on jaettu useampaan luokkaan, joilla on oma vastuualueensa.
- UI: kommunikoi käyttäjän kanssa.
- FileHandler: suorittaa kaikki tiedostoihin liittyvät operaatiot.
- HuffmanCoding: toteuttaa Huffman koodauksen pakkaus- ja purkualgoritmit.
- LZW: toteuttaa Lempel-Ziv-Welchin pakkaus- ja purkualgoritmit.
- CompressionComparator: vertailee algoritmien suorituskykyä keskenään.


## Huffman koodaus
Huffmanin koodaus on luotu seuraavien pseudokoodien mukaisesti: 

### Pakkaaminen

Pseudokoodi:

1. Lasketaan kirjainten frekvenssit tekstistä.
2. Luodaan jokaisesta kirjaimesta oma solmu(kirjain, frekvenssi, vasenLapsi, oikeaLapsi)
3. Lisätään solmut minimikekoon frekvenssin perusteella.
4. Niin kauan kun minimikeossa on yksi tai useampi solmu:
    - poista kaksi ensimmäistä solmua minimikeosta
    - luo uusi solmu, jonka frekvenssi on yhdistettävien solmujen frekvenssien summa. Lisää yhdistetyt solmut uuden solmun lapsiksi.
    - Lisää uusi solmu minimikekoon
5. Jäljelle jäänyt solmu on Huffmanin puun juuri.
6. Muodostetaan huffmanin koodit kirjaimille:
    - Aloitetaan puun juuresta ja asetetaan koodiksi tyhjä merkkijono
    - Tutkitaan puuta rekursiivisesti:
        - Jos solmulla on vasen lapsi, lisätään "0" huffmanin koodiin.
        - Jos solmulla on oikea lapsi, lisätään "1" huffmanin koodiin.
    - Kun saavutaan lehteen (eli solmuun, jossa kirjain), lisätään kirjain ja muodostettu huffmanin koodi sanakirjaan.
7. Koodataan teksti vastaamaan muodostettuja Huffmanin koodeja.
8. Luodaan merkkijonoesitys, johon muodostettu puu on tallennettu.


### Purkaminen

1. Luetaan bittejä tallennetusta huffmanin puun esitysmuodosta:
    - Jos bitti on 1, luetaan seuraavat 16-bittiä ja saadaan kirjain. Luodaan uusi lehti, jolla ei ole lapsia.
    - Jos bitti on 0, tutkitaan rekursiivisesti samalla logiikalla molemmat lapsisolmut, ja luodaan uusi solmu asettaen lapsisolmut sille.
2. Jäljelle jäänyt solmu on Huffmanin puun juuri.
3. Muodostetaan huffmanin koodit kirjaimille:
    - Aloitetaan puun juuresta ja asetetaan koodiksi tyhjä merkkijono
    - Tutkitaan puuta rekursiivisesti:
        - Jos solmulla on vasen lapsi, lisätään "0" huffmanin koodiin.
        - Jos solmulla on oikea lapsi, lisätään "1" huffmanin koodiin.
    - Kun saavutaan lehteen (eli solmuun, jossa kirjain), lisätään muodostettu huffmanin koodi ja kirjain sanakirjaan.
4. Puretaan koodi korvaamalla huffmanin koodit niitä vastaavalla kirjaimella.

## LZW

Algoritmi on luotu seuraavien pseudokoodien mukaisesti.

### Pakkaaminen

*     PSEUDOCODE
1     Initialize table with single character strings
2     P = first input character
3     WHILE not end of input stream
4          C = next input character
5          IF P + C is in the string table
6            P = P + C
7          ELSE
8            output the code for P
9          add P + C to the string table
10           P = C
11         END WHILE
12    output code for P 

### Purkaminen

*    PSEUDOCODE
1    Initialize table with single character strings
2    OLD = first input code
3    output translation of OLD
4    WHILE not end of input stream
5        NEW = next input code
6        IF NEW is not in the string table
7               S = translation of OLD
8               S = S + C
9       ELSE
10              S = translation of NEW
11       output S
12       C = first character of S
13       OLD + C to the string table
14       OLD = NEW
15   END WHILE


## Saavutetut aika- ja tilavaativuudet

Huffman koodauksen aikavaativuus on O(n log n).
LZW-algoritmin aikavaativuus on O(n).

## Parannusehdotukset

Käyttöliittymä voisi olla graafinen ja olla mahdollisuus myös lisätä uusia teksitiedostoja.

## Kielimallien käyttö

Projektissa on hyödynnetty chatGPT 3.5 ilmaisversiota suunnittelussa ja dokumentaation kielioppitarkistuksessa. Suunnitteluvaiheessa tekoälyä on hyödynnetty siten, että kysymyksen asettelu on tyyppiä "Ajattelin tehdä asian x tavalla y, mutta voisiko tapa z olla myös toimiva, mitkä ovat plussat ja miinukset näillä tavoilla?". Esimerkiksi ohjelman yleisrakenteen suunnittelussa tästä oli jonkin verran hyötyä.

Koska käytetyt algoritmit eivät olleet minulle entuudestaan tuttuja, pyysin myös tekoälyä selittämään tarkasti mitä missäkin vaiheessa pseudokoodia tehdään ja miksi, jotta ymmärsin paremmin algoritmien toimintaa. Tämä ei tosin ollut riittävän kattavasti selitetty ja oikeastaan mm. Youtubesta löytyvät opetusvideot aiheista olivat parempia oppimismielessä.

Projektin alkuvaiheessa hyödynsin myös tekoälyä tarkistamaan jotkin lauseet doctsringeistä, joiden kieliopin oikeellisuutta epäilin. Projektin edetessä en kokenut tälle enää tarvetta, sillä selkeästi tietynlainen rutiini tähän kehittyi ja usko omaan osaamiseen ilmeisesti kasvoi. Tämä oli ehkä suurin tekoälyn tuottama hyöty tässä projektissa, muutoin siitä ei ollut kauheasti hyötyä.

### Viitteet

Huffman-koodaus
- [GeeksForGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/time-and-space-complexity-of-huffman-coding-algorithm/)

- [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

Lempel-Ziv-Welch
- [Wikipedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [GeeksForGeeks](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/)