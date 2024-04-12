### Viikkoraportti 4

Tämä viikko on mennyt LZW-algoritmin toteuttamiseen. Koska edellisellä viikolla taistelin binääritiedostojen kanssa, nyt ongelmia ei tämän suhteen ollut, sillä lzw-algoritmin avulla pakattava data oli huomattavan paljon helpompi tallentaa binäärimuodossa tiedostoon ja myös parsia sieltä ulos. Käyttöliittymään on lisätty myös nyt mahdollisuus valita kumpaa algoritmia käytetään. Käyttöliittymä on eriytetty omaksi UI-luokakseen, joka on vastuussa käyttäjän kanssa kommunikoinnista. Tiedostojen käsittelyyn on luotu oma FileHandler-luokka, joka on vastuussa kaikista tiedostoihin liittyvistä toiminnoista. CompressionComparator-luokka vastaa molempien algoritmien suorittamisesta ja datan vertailusta. Kyseisen luokan toiminta laajenee tulevilla viikoilla.

tällä viikolla vielä:
- testejä
- docstrings
- toteutusdokumentti

Ensi viikolla tarkoitus:
- lisätä tietoa pakatun tiedoston koosta ym. muuta dataa
- lisää testejä
- isommat tiedostot

Tuntikirjanpito: \
8.4. 1h \
9.4. 5h \
10.4. 4h \
11.4. 5h \
12.4. aloitus 09:08 - 