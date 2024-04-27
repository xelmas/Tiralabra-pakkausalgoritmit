# Testausdokumentaatio

## Yksikkötestit

Yksikkötesteillä on testattu testidatan avulla yksittäisten funktioiden toimintaa Huffman- ja LZW-luokista. Testikattavuuden ulkopuolelle on jätetty tiedostojen käsittelystä vastaava luokka Filehandler sekä käyttöliittymäluokka UI ja vertailusta vastaava luokka CompressionComparator. Näiden luokkien testaaminen ei ole mielekästä tässä projektissa.

## Invarianttitestaus

### HuffmanCoding-luokka

Testattu Huffman-luokan koodi käyttäen Hypothesis-kirjastoa invarianttitestaukseen. Invarianttitestauksella on luotu erilaisia ja eripituisia merkkijonoja, ja on testattu, että Huffman koodauksen algoritmi luo sanakirjan kirjainten esiintyvyystiheydestä oikein kaikilla syötteillä. Invarianttitestauksella on myös testattu, että erilaiset sanakirjat kirjainten esiintyvyystiheydestä muodostavat minimikeon yhdenmukaisesti.

Molempiin testeihin on lisätty example-arvot, jotka testataan aina testien suorituksen yhteydessä. Tässä tapauksessa testataan, että sanakirja ja minimikeko luodaan yhdenmukaisesti, vaikka teksitiedosto olisi vain yhden merkin mittainen.
Myös solmujen yhdistäminen on testattu, jotta Huffmanin puu luodaan yhdenmukaisesti.

Algoritmin pakkaus- ja purku on testattu yhdenmukaiseksi erilaisilla syötteillä. Eli syötteenä saatu teksti pakataan ja se on purkamisen jälkeen täsmälleen samanlainen kuin ennen pakkaamista.

### LZW-luokka

Testattu LZW-luokan koodi käyttäen Hypothesis-kirjastoa invarianttitestaukseen. Invarianttitestauksella on luotu erilaisia ja eripituisia syötteitä,
joilla on todettu pakkaus- ja purkualgoritmin toimivan yhdenmukaisesti. Eli syötteenä saatu teksti pakataan ja se on purkamisen jälkeen täsmälleen samanlainen kuin ennen pakkaamista. Lisäksi on testattu, että ekstramerkit lisätään sanakirjaan yhdemukaisesti ja maksimipituus bittien määräälle lasketaan oikein erilaisilla syötteillä.

## Testikattavuusraportti

Tämän hetken tila:

![Testikattavuus](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/coverage_report6.png)

## Mitä testattu ja miten?
Tässä vaiheessa projektia on testattu, että 1,7 kilotavun tiedosto (text.txt) on täsmälleen saman kokoinen purkamisen jälkeen molemmilla algoritmeilla. Pakatun tiedoston koko taas on Huffman koodauksen jälkeen 945 tavua, mikä on huomattavasti pienempi kuin alkuperäinen. Pakatun tiedoston koko taas LZW-algoritmilla on 1,2 kilotavua, mikä on myös pienempi kuin alkuperäinen, mutta ei yhtä tehokas tällä testisyötteellä kuin Huffman koodauksella suoritettu.

Toinen testitiedosto (text2.txt), jota on käytetty apuna LZW-algoritmin toteutuksessa, antaa hyvän kuvan siitä, että pienillä tekstitiedostoilla pakkaaminen ei välttämättä aina ole järkevää. Tiedosto on vain 18 tavun kokoinen, joka Huffman koodauksella saadaan pakattua 16 tavun kokoiseksi, mutta LZW-algoritmilla myös pakatun tiedoston koko on sama 18 tavua.

Molempien algoritmien toiminta on testattu myös isolla sample.txt tiedostolla (1,1 megatavua). Huffman koodauksella saadaan tiedosto pakattua 47 % pienemmäksi kuin alkuperäinen tiedosto ja LZW-algoritmilla jopa 71 % pienemmäksi.

Ohjelma ei yritä pakata tai purkaa tyhjää tiedostoa.

