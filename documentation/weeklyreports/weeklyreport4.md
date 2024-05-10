### Viikkoraportti 4

Tämä viikko on mennyt LZW-algoritmin toteuttamiseen. Koska edellisellä viikolla taistelin binääritiedostojen kanssa, nyt ongelmia ei tämän suhteen ollut, sillä lzw-algoritmin avulla pakattava data oli huomattavan paljon helpompi tallentaa binäärimuodossa tiedostoon ja myös parsia sieltä ulos. Käyttöliittymään on lisätty myös nyt mahdollisuus valita kumpaa algoritmia käytetään. Käyttöliittymä on eriytetty omaksi UI-luokakseen, joka on vastuussa käyttäjän kanssa kommunikoinnista. Tiedostojen käsittelyyn on luotu oma FileHandler-luokka, joka on vastuussa kaikista tiedostoihin liittyvistä toiminnoista. CompressionComparator-luokka vastaa molempien algoritmien suorittamisesta ja datan vertailusta. Kyseisen luokan toiminta laajenee tulevilla viikoilla.

Toteutusdokumentti on aloitettu. Ensi viikolla tarkoitus laajentaa CompressionComparator luokkaa, joka koostaa tietoa algoritmien suorituskyvystä ym. Tämän lisäksi pitäisi löytää jokin iso tekstitiedosto, jota käyttää testeissä, sillä nykyiset tiedostot ovat hyvin pieniä. Lisäksi testausta tulisi laajentaa, mutta se voi olla, että siirtyy vielä viikolla eteenpäin.

#### Tuntikirjanpito

| Päivä       | Tuntimäärä (h) |
| ----------- | -----------    |
| 8.4.        | 1              |
| 9.4.        | 5              |
| 10.4.       | 4              |
| 11.4.       | 5              |
| 12.4.       | 4              |
| Yhteensä    | 19             |