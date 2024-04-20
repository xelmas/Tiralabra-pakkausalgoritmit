### Viikkoraportti 5

Tällä viikolla aikaa on kulunut testaukseen. Invarianttitestaus ei ollut minulle vielä tuttua, joten Hypothesis-kirjaston dokumentaatioon tutustuminen on vienyt jonkin aikaa. Invarianttitestaus on aloitettu Huffman koodaus-luokalle. Tällä viikolla olen myös refaktoroinut koodia ja luonut toiminnallisuutta CompressionComparator-luokkaan, joka on vastuussa tiedoston pakkaamisesta ja purkamisesta algoritmeilla. Se antaa halutulle algoritmille parametrina tiedostosta luetun datan pakattavaksi tai purettavaksi, ja saa algoritmilta datan takaisin kirjoitettavaksi tiedostoon. Luokka myös mahdollistaa vertailufunktion compare, joka ajaa molemmille algoritmeille pakkaus- ja purkualgoritmit ja tallentaa statistiikat listaan. Käyttöliittymään on lisätty mahdollisuus valita vaihtoehto, joka pakkaa ja purkaa syötetyn tiedoston molemmilla algoritmeilla, ja tulostaa statistiikat käyttäjälle.

Molempien algoritmien toiminta on testattu myös isolla tiedostolla (1,1 megatavua). Kyseinen sample.txt-tiedosto on luotu Lorem ipsum generaattoria hyödyntäen. Aluksi koitin käyttää plain text tiedostoa Seitsemästä veljeksestä, mutta kyseinen tiedosto sisältää sellaisia unicode-merkkejä, että LZW-sanakirjan luominen tukemaan näitä kaikkia ei tunnu olevan järkevää, sillä sanakirjaan pitäisi alustaa 1 114 112 erilaista merkkiä ja niiden koodit tulisi tallentaa vähintään 21 bittisinä. Jos haluaisi hyödyntää kaikkia mahdollisia merkkejä, tulisi sanakirja välillä tyhjentää. Tätä en ainakaan tällä hetkellä ole ajatellut implementoida algoritmiini, joten siksi tekstitiedostoksi on valittu sellainen, jonka sisältö vastaa algoritmin tukemaa laajennettua ASCII-merkistöä (0-255).

Kysymys ohjaajalle liittyen ylläolevaan kappaleeseen: Onko hyväksyttävää luoda algoritmi, joka tukee vain laajennettua ascii-merkistöä, vai onko parempi luoda tuollainen kaikki unicode pointsit tukeva sanakirja (ilman optimointia eli sanakirjan tyhjentämistä välissä)?

Ensi viikolla tarkoitus ainakin lisätä testejä, kuten invarianttitestaus LZW-luokasta ja refaktoroida koodia.

Tuntikirjanpito \
15.4. 2h30min \
16.4. 3h \
17.4. 3h \
18.4. 5h \
19.4. 5h \
20.4. 4h \
Yhteensä: 22h30min