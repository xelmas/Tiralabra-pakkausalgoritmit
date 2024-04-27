### Viikkoraportti 6

Yksittäisten algoritmien suorituskykyä mittaavat statistiikat taulukoidaan myös suorituksen jälkeen, aiemmin tämä oli vain käytössä kun vertaillaan algoritmeja. Jos käyttäjä ensin pakkaa tiedoston Huffmanin koodaus-algoritmilla, taulukkoon tulee sarakkeen "decompression time" kohdalle luku 0.0, mikä tarkoittaa, että purkamista ei ole suoritettu. Kun käyttäjä seuraavaksi purkaa tiedoston, päivitetään samaan taulukkoon kyseisen algoritmin kohdalle myös purkamiseen kulunut aika. CompressionComparator-luokkaa on refaktoroitu siten, että benchmark metodi on jaettu pienempiin osiin, jotta samoja metodeja voidaan käyttää yksittäisen algoritmin kohdalla että hyödyntäen compare-metodia.

Tiedostoon utils.py on lisätty useamman luokan tarvitsema muuttuja FILE_DIRECTORY, joka osoittaa polun pakattaviin ja purettaviin tekstitiedostoihin. Samaan tiedostoon on myös siirretty molemmissa algoritmiluokissa ollut metodi add_padding, jotta koodi ei olisi toisteista.

Ohjelman rakennetta on muokattu selkeämmäksi; algoritmien toteutuksesta vastaavat tiedostot ovat omassa kansiossaan, kuten myös teksitiedostot. Lisäksi utils.py tiedosto ja filehandler.py tiedosto ovat omassa kansiossaan utilities. Tämän antaa selkeämmän rakenteen projektin lähdekoodille, ja tärkeimmät komponentit main.py, ui.py ja compression_comparator.py ovat juuressa.

Luodut tiedostot poistetaan ohjelman suorituksen loputtua. Ohjelman toimintaan on lisätty ominaisuus, että pakattu binääritiedosto poistetaan purkamisen yhteydessä ja tilalle luodaan teksitiedosto decompressed_text. Myös tämä tiedosto poistetaan, kun ohjelman suoritus päättyy.

LZW-luokkaan on lisätty invarianttitestejä. Invarianttitestauksella on testattu, että pakkaaminen ja purkaminen tuottaa saman lopputuloksen, ekstramerkit lisätään sanakirjaan yhdemukaisesti ja maksimipituus bittien määräälle lasketaan oikein erilaisilla syötteillä.

Viime viikolla ongelmaksi koitui se, että millä arvoilla LZW-algoritmin sanakirja tulisi alustaa, jotta voidaan pakata tekstitiedostoja, joissa on myös muita merkkejä kuin ascii-merkistöä 0-255. Koin haasteelliseksi löytää sopivaa tiedostoa testattavaksi, joten ratkaisin ongelman siten, että nyt ohjelma tukee kaikkia mahdollisia unicode-merkkejä, joita tekstissä esiintyy. Ennen kuin LZW-algoritmin sanakirja alustetaan, tekstitiedostosta poimitaan kaikki sellaiset merkit listaan, jotka eivät kuulu välillä 0-255. Sanakirjan alustuksessa lisätään nämä ekstramerkit myös sanakirjaan siten, että ensimmäinen ekstramerkki saa arvokseen 256 ja seuraava 257 jne. Tämä mahdollistaa sen, että testitiedostoina voidaan käyttää Project Gutenbergistä ladattuja teoksia, mutta ei tarvitse kuitenkaan alustaa sanakirjaan kaikkia mahdollisia utf-8 merkkejä. Vertasin suorituskykyä keskenään sille, että alustetaan kaikki mahdolliset merkit tai sitten vain tarvittavat, ja jälkimmäinen oli tehokkaampi tapa.

Toteutus- ja testausdokumentit jäivät vielä kesken, joten niitä on tarkoitus ensi viikolla vielä täydentää.


Tuntikirjanpito \
21.4. 4h30min \
22.4. 4h \
23.4. 2h30min \
24.4. 5h30min \
25.4. 5h \
26.4. 6h \
27.4. 3h \
Yhteensä: 30h 30min