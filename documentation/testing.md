# Testausdokumentaatio

## Yksikkötestit

Yksikkötesteillä on testattu testidatan avulla yksittäisten funktioiden toimintaa Huffman- ja LZW-luokista. Yksikkötesteihin on lisätty myös utilities-tiedoston apufunktioiden toiminnan testaus molemmilla algoritmeilla sekä CompressionComparator luokan toiminta. Testikattavuuden ulkopuolelle on jätetty käyttöliittymäluokka UI sekä toimintalogiikan toteutus main-tiedostosta. Näiden testaaminen ei ole mielekästä tässä projektissa.

Yksikkötesteillä on testattu, että pakattu ja sitten purettu teksti on täysin samansisältöinen molemmilla algoritmeilla kuin alkuperäinen teksti. Lisäksi on testattu, että ohjelma ei yritä purkaa tai pakata tyhjää tekstiä. Lisäksi on testattu, että pakattavassa muodossa oleva tietue on samankokoinen, vaikka samaa tekstiä pakataan useamman kerran peräkkäin.

#### HuffmanCoding-luokka

Mikäli tekstitiedosto on vain yhden merkin mittainen, on testattu, että Huffmanin koodi kyseiselle merkille on oletusarvoisesti "0". 

Huffmanin puun luontiin tarvittavat metodit, eli sanakirjan luonti kirjainten esiintyvyystiheydestä ja sen avulla minimikeon luonti ja solmujen yhdistäminen on testattu toimivan oikein. Yksikkötesteillä on testattu, että alussa minimikeon ensimmäinen solmu ja sen frekvenssi vastaavat odotettuja arvoja. Lisäksi minimikeon solmujen yhdistäminen on testattu toimivan oikein, koska jäjelle jääneen Huffmanin puun juuren frekvenssiarvo on todettu vastaavan odotettua. Lisäksi on testattu, että Huffmanin koodit vastaavat odotettuja arvoja annetulla testisyötteellä.

Yksikkötesteillä on myös testattu, että pakattu teksti ja tietue Huffmanin puusta on muodostettu oikein annetulla testisyötteellä. Lisäksi näiden yhdistelmästä muodostettu tietue, joka kirjoitetaan tiedostoon, on testattu vastaavan odotettua. Lisäksi on testattu, että tästä kokonaistietueesta saadaan parsittua tiedot ulos ja ne vastaavat samoja arvoja kuin pakatessa. Myös puretun tekstin avulla muodostetun Huffmanin puun juuri on testattu olevan sama kuin pakatessakin.

Yksikkötesteillä on testattu, että kokonaistietueen koko määrittää oikein minimilukumäärän kuinka monella bitillä kyseinen tieto tulee vähintään ilmaista. Lisäksi on testattu, että myös suurin unicode-arvo määrittää oikein kuinka monella bittimäärällä vähintään jokainen kirjain on tallennettava tietueeseen.

#### LZW-luokka

LZW:n sanakirjan alustus on testattu yksikkötesteillä toimivan oikein sekä pakkaamisen että purkamisen yhteydessä. Ennen pakkaamista muodostettu sanakirja on testattu koostuvan kirjaimista ja niitä vastaavista koodeista, ja purkamista varten muodostettu sanakirja on muodostettu koostuvan koodeista ja niitä vastaavista kirjaimista. Lisäksi on testattu, että sanakirjoihin alustetaan ekstramerkit, mikäli sellaisia on.

Yksikkötesteillä on myös testattu, että pakattu teksti on muodostettu oikein listaan, joka koostuu numeroista, jotka vastaavat tekstisyötteen merkkejä/sekvenssejä. On testattu, että numerot muutetaan binääriesitysmuotoon ja muodostetaan kokonaistietue odotetulla tavalla. Lisäksi on testattu, että tästä kokonaistietueesta saadaan parsittua tiedot ulos ja ne vastaavat samoja arvoja kuin pakatessa. Puretusta datasta muodostettu lista on testattu olevan sama kuin pakatessakin muodostettu lista, ja että purkamisen yhteydessä muodostettu teksti vastaa alkuperäistä.

Yksikkötesteillä on testattu, että suurin sanakirjan lukuarvo kuinka monella bittimäärällä vähintään jokainen numero on tallennettava tietueeseen määritetään oikein.

#### CompressionComparator-luokka

Yksikkötesteillä on testattu compare-metodin toiminta molemmilla algoritmeilla. Metodin on testattu palauttavan statistiikat odotetunlaisesti eikä purkamisen yhteydessä ole tapahtunut virhettä. Lisäksi on testattu, että ainoastaan ei-tyhjät tekstitiedostot valitaan listaan pakattavaksi.

## Invarianttitestaus

### HuffmanCoding-luokka

Huffman-luokan toimintaa on testattu käyttäen Hypothesis-kirjastoa invarianttitestaukseen. Invarianttitestauksella on luotu erilaisia ja eripituisia merkkijonoja, ja on testattu, että Huffman koodauksen algoritmi luo sanakirjan kirjainten esiintyvyystiheydestä oikein kaikilla syötteillä. Invarianttitestauksella on myös testattu, että erilaiset sanakirjat kirjainten esiintyvyystiheydestä muodostavat minimikeon yhdenmukaisesti.

Molempiin testeihin on lisätty example-arvot, jotka testataan aina testien suorituksen yhteydessä. Tässä tapauksessa testataan, että sanakirja ja minimikeko luodaan yhdenmukaisesti, vaikka teksitiedosto olisi vain yhden merkin mittainen. Myös solmujen yhdistäminen on testattu, jotta Huffmanin puu luodaan yhdenmukaisesti. Testit varmistavat myös, että tietue Huffmanin puusta on minimibittien lukumäärän pituinen. Tämä on testattu erilaisilla tekstisyötteillä, että puun tallennukseen tarvittava bittimäärä on yhdenmukainen, eikä uudelleenpakkaaminen kasvata tietueen kokoa. 

Algoritmin pakkaus- ja purku on testattu yhdenmukaiseksi erilaisilla syötteillä. Eli syötteenä saatu teksti pakataan ja se on purkamisen jälkeen täsmälleen samanlainen kuin ennen pakkaamista.

### LZW-luokka

LZW-luokan toimintaa on testattu käyttäen Hypothesis-kirjastoa invarianttitestaukseen. Invarianttitestauksella on luotu erilaisia ja eripituisia syötteitä, joilla on todettu pakkaus- ja purkualgoritmin toimivan yhdenmukaisesti. Eli syötteenä saatu teksti pakataan ja se on purkamisen jälkeen täsmälleen samanlainen kuin ennen pakkaamista. Lisäksi on testattu, että ekstramerkit lisätään sanakirjaan yhdemukaisesti ja maksimipituus bittien määräälle lasketaan oikein erilaisilla syötteillä.

## Automaatiotestit

CompressionComparator-luokan automaatiotestit suorittavat pakkaus- ja purkualgoritmit kaikille tekstitiedostoille. Testeissä testataan, että pakkaus- ja purkustatistiikat ovat odotetunlaisia eikä purkamisen yhteydessä ole tapahtunut virhettä. Testeissä varmistetaan myös, että purkamisaika tallennetaan taulukkoon oikein pakkaamisen jälkeen ja, että purettu tiedosto on täsmälleen samankokoinen kuin alkuperäinen tiedosto.

## Testikattavuusraportti

![Testikattavuus](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/images/coverage_report_final.png)

## Mitä testattu ja mitä havaitaan?

Taulukoituna yhden testiajon tekstitiedostojen pakkaus- ja purkustatistiikat käyttäen Huffman koodausta ja LZW-algoritmia.

|                                |           |   Huffman       |                |                  | LZW            |                |                  |
|------------------------------- |-----------|-----------------|----------------|------------------|----------------|----------------|------------------|
| Filename                       | Size (kB) | Comp. ratio (%) | Comp. time (s) | Decomp. time (s) | Comp. ratio (%)| Comp. time (s) | Decomp. time (s) |
|onechar.txt                     | 0.0039    | -100.0000       | 0.0002         | 0.0002           | 25.0000        | 0.0001         | 0.0001           |
|sample1.txt                     | 0.0176    | 16.6667         | 0.0001         | 0.0001           | 22.2222        | 0.0001         | 0.0001           |
|sample2.txt                     | 0.0195    | 20.0000         | 0.0002         | 0.0001           | 25.0000        | 0.0001         | 0.0001           |
|symbolic_logic.txt              | 448.1748  | 42.9977         | 0.1150         | 0.2144           | 61.9893        | 0.2748         | 0.0951           |
|seitseman_veljesta.txt          | 661.9785  | 46.0088         | 0.1416         | 0.2727           | 55.4194        | 0.3882         | 0.1516           |
|principia_mathematica_latin.txt | 817.6406  | 41.3146         | 0.1917         | 0.3631           | 57.2966        | 0.4855         | 0.2062           |
|epic_poem_of_finland.txt        | 824.6025  | 42.7755         | 0.1908         | 0.3670           | 58.8520        | 0.4487         | 0.1773           |
|life_of_a_philosopher.txt       | 864.7090  | 42.7773         | 0.2011         | 0.3876           | 57.2463        | 0.5959         | 0.1935           |
|kevat_ja_takatalvi.txt          | 895.7832  | 47.3883         | 0.1991         | 0.3641           | 58.0314        | 0.5162         | 0.1993           |
|lorem_ipsum.txt                 | 1046.3379 | 46.5443         | 0.2448         | 0.4430           | 71.0225        | 0.5325         | 0.2052           |
|book_of_han_chinese.txt         | 2643.3857 | 60.8104         | 0.4270         | 0.8959           | 59.1378        | 3.9022         | 0.5574           |
|monte_cristo.txt                | 2661.6387 | 44.5189         | 0.6355         | 1.2155           | 62.4688        | 1.6185         | 0.5809           |
|les_miserables.txt              | 3218.3848 | 43.7268         | 0.7386         | 1.4831           | 59.3680        | 2.1128         | 0.7187           |


Taulukko kertoo sen, että pakkaus- ja purkualgoritmit ovat onnistuneesti suoritettu kaikilla tiedostoilla, ja purettu tiedosto on täysin samanlainen kuin alkuperäinen tiedosto. Mikäli virhe olisi tapahtunut, olisi algoritmin statistiikkasarakkeissa arvoina "None", "None", "None".

Yleisesti voidaan sanoa, että LZW-algoritmi suoriutuu paremmin kuin Huffman koodaus tällä testidatalla. Kun jätetään pienet tiedostot huomiotta, Huffman koodauksen pakkausteho vaihtelee 41-60 % välillä ja LZW:n pakkausteho 55-71 % välillä. Mielenkiintoista on myös havaita, että Huffman koodaus suoriutuu pakkaamisesta lähes kaksi kertaa nopeammin kuin LZW, kun taas LZW suorittaa purkamisen noin puolet nopeammin kuin Huffman koodaus. Kokonaisaikaa tarkasteltuna Huffman koodaus on kuitenkin nopeampi kuin LZW kaikilla testitapauksilla. Ero selittyy sillä, että pakkaamisvaiheessa LZW:llä menee aikaa sanakirjan päivittämiseen ja laajentamiseen, kun taas Huffmanin puun luominen minimikeon avulla on nopeaa.

Englanninkieliset teokset "epic_poem_of_finland", "les_miserables" ja "monte_cristo" ovat valittu testidataan, koska ne ovat suuria luonnollista kieltä sisältäviä tiedostoja. Algoritmit suoriutuvat teosten pakkaamisesta suhteellisen hyvin, tosin LZW huomattavan paljon tehokkaammin.

Suomenkieliset teokset "seitseman_veljesta" ja "kevat_ja_takatalvi" pakkautuvat Huffman koodauksella hieman tehokkaammin kuin edeltävät englanninkieliset teokset samalla algoritmilla. LZW:n kohdalla taas ei ole havaittavissa eroja pakkaustehossa, oli sitten kyseessä suomen- tai englanninkielinen tekstitiedosto.

Tekstitiedostot "symbolic logic", "principia_mathematica_latin" ja "life_of_a_philosopher" ovat valittu testidataan siksi, koska ne sisältävät matemaattisia merkkejä, joita ei romaaneissa tyypillisesti ole. Algoritmit suoriutuvat kuitenkin näidenkin tiedostojen pakkaamisesta suhteellisen hyvin, tosin Huffman koodaus hieman heikommalla pakkausteholla kuin LZW.

Yllättäen kuitenkin Huffman koodaus suoriutuu kiinankielisestä teoksesta "Book of Han" hieman paremmin kuin LZW. Huffman koodauksen pakkausteho on 60 % ja LZW:n 59 %. Tämä viittaa siihen, että tekstissä on hyvin vähän toisteisuutta, jolloin LZW:n tehokkuus ei nouse esiin. Myös pakkaamiseen käytetty aika LZW:llä on huomattavan suuri, jopa 3.9 sekuntia, kun taas Huffmanilla se on 0.43 sekuntia. Tästä havaitaan, että mikäli tekstistä puuttuu toisteiset merkkijonot, LZW algoritmin pakkausaika kasvaa, sillä se joutuu jatkuvasti päivittämään ja kasvattamaan sanakirjaa.

Tekstitiedosto "lorem_ipsum" taas on niin toisteista, että sen vertailu on hieman epäreilua, sillä odotetustikin LZW suoriutuu tästä hyvin tehokkaasti ja saavuttaa parhaimman pakkaustehonsa 71 %. Koska kyseessä on niin toisteinen teksti, tämän voi melkein jättää vertailussa huomiotta. Halusin sen tähän kuitenkin jättää, jotta LZW:n tehokkuus tulee testeissä ilmi.

Pienet tekstitiedostot ovat esimerkkinä siitä, että niiden pakkaaminen ei välttämättä ole kovin järkevää. Tekstitiedosto "onechar" sisältää vain yhden merkin, jonka unicode-arvo on desimaalina 73728. Tämä aiheuttaa sen, että Huffman koodauksen tietue Huffmanin puusta kasvattaa tiedoston kokoa jopa kaksinkertaiseksi kuin itse alkuperäinen tiedosto, minkä takia pakkausteho on -100 %. LZW suoriutuu tästä selkeästi paremmin kuin Huffman koodaus, mutta toki heikommin kuin keskimäärin, sillä sen pakkausteho on vain 25 %. Lisäksi toiset pienet tekstitiedostot havainnollistavatkin sitä, että pienten tekstitiedostojen pakkaamisella ei välttämättä saavuteta kovin suurta hyötyä, sillä pienet tiedostot "sample1" ja "sample2" saadaan pakattua vain noin 22-25 % alkuperäistä pienemmiksi.