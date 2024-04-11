# Testausdokumentaatio

## Yksikkötestit

Yksikkötesteillä on testattu testidatan avulla yksittäisten funktioiden toimintaa Huffman- ja LZW-luokista. Testikattavuuden ulkopuolelle on jätetty tiedostojen käsittelystä vastaava luokka Filehandler sekä käyttöliittymäluokka UI ja pakkausalgoritmien tehokkuutta vertaileva luokka CompressionComparator. Näiden luokkien testaaminen ei ole mielekästä tässä projektissa.

### Testikattavuusraportti

Tämän hetken tila:

![Testikattavuus](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/coverage_report4.png)

### Mitä testattu ja miten?
Tässä vaiheessa projektia on testattu, että 1,7 kilotavun tiedosto on täsmälleen saman kokoinen purkamisen jälkeen. Pakatun tiedoston koko taas on 945 tavua, mikä on huomattavasti pienempi kuin alkuperäinen tällä testisyötteellä.

