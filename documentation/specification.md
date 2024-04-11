# Vaatimusmäärittely

Helsingin yliopiston aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssi. Tutkinto-ohjelma: Tietojenkäsittelytieteen kandidaatti.

Projekti on toteutettu Pythonilla, mutta pystyn myös vertaisarvioimaan Javalla toteutettuja projekteja.
Projektissa käytetty kieli on englanti, mutta dokumentaatio on kirjoitettu suomeksi.

## Projektin aihe

Aiheena on toteuttaa kaksi erilaista häviötöntä pakkaus- ja purkausalgoritmia ja vertailla niiden suorituskykyä keskenään, kun pakattava/pakattu tiedosto on luonnollista kieltä sisältävä teksti. Tavoitteena on saada pakattua tiedosto 40-60 % alkuperäisestä koosta. 

## Algoritmit

Projektiin on valittu vertailtaviksi Huffman-koodaus ja Lempel-Ziv LZW-algoritmi.

### Viitteet

Huffman-koodaus
- [GeeksForGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

Lempel-Ziv LZw
- [Wikipedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [GeeksForGeeks](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/)

## Toiminnallisuudet

- Ohjelman käyttöliittymä on toteutettu komentorivillä.
- Ohjelma pystyy pakkaamaan ja purkamaan luonnollista kieltä sisältäviä tekstitiedostoja valituilla algoritmeilla.
- Ohjelma luo tehokkaasti kiintolevylle tiedoston, joka sisältää kaiken purkamiseen tarvittavan datan.
- Pakkaamisen tai purkamisen jälkeen ohjelma tulostaa komentoriville dataa suorituksesta, minkä perusteella voidaan vertailla eri algoritmien suorituskykyä.
