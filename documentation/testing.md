# Testausdokumentaatio

## Yksikkötestit

Yksikkötesteillä on testattu testidatan avulla yksittäisten funktioiden toimintaa Huffman- ja LZW-luokista. Testikattavuuden ulkopuolelle on jätetty tiedostojen käsittelystä vastaava luokka Filehandler sekä käyttöliittymäluokka UI. Näiden luokkien testaaminen ei ole mielekästä tässä projektissa. CompressionComparator luokka on jätetty vielä pois testikattavuudesta, sillä sen varsinainen toteutus ja muoto on vielä kesken. Aluksi oli ajatus, että kyseinen luokka jää myös testien ulkopuolelle, mutta asia selvinnee myöhemmin.

### Testikattavuusraportti

Tämän hetken tila:

![Testikattavuus](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/coverage_report4.png)

### Mitä testattu ja miten?
Tässä vaiheessa projektia on testattu, että 1,7 kilotavun tiedosto (text.txt) on täsmälleen saman kokoinen purkamisen jälkeen molemmilla algoritmeilla. Pakatun tiedoston koko taas on Huffman koodauksen jälkeen 945 tavua, mikä on huomattavasti pienempi kuin alkuperäinen. Pakatun tiedoston koko taas LZW-algoritmilla on 1,2 kilotavua, mikä on myös pienempi kuin alkuperäinen, mutta ei yhtä tehokas tällä testisyötteellä kuin Huffman koodauksella suoritettu.

Toinen testitiedosto (text2.txt), jota on käytetty apuna LZW-algoritmin toteutuksessa, antaa hyvän kuvan siitä, että pienillä tekstitiedostoilla pakkaaminen ei välttämättä aina ole järkevää. Tiedosto on vain 18 tavun kokoinen, joka Huffman koodauksella saadaan pakattua 16 tavun kokoiseksi, mutta LZW-algoritmilla myös pakatun tiedoston koko on sama 18 tavua.

