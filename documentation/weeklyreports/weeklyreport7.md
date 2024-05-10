### Viikkoraportti 7

Viimeisellä viikolla on lisätty uusia tekstitiedostoja testattavaksi, kuten kiinan kielinen "Book of Han"-teos sekä tekstitiedosto, joka sisältää vain yhden merkin, jonka unicode-arvo on kohtuullisen suuri. Nämä lisättyäni havaitsin bugin Huffmanin koodissa "headerin" luonnin yhteydessä. Headeriin tallennetaan luotu Huffmanin puu muodossa, josta se voidaan luoda uudestaan. Headerissä oli varattu yksittäiselle kirjaimelle 16 bittiä, jolla se voidaan ilmaista. Kävi ilmi, että se ei välttämättä riitä, joten muokkasin koodia nyt niin, että myös Huffmanin koodissa määritetään mikä on minimibittimäärä, jolla isoin unicode-arvo voidaan ilmaista ja kaikki kirjaimet tallennetaan tämän minimibittimäärän mukaisesti. Lisäksi on lisätty tiedosto principia_mathematica, joka on latinan kielinen teos, jossa on matemaattisia kaavoja sekä tiedosto symbolic_logic, joka myös sisältää erilaisia merkkejä kuin tavalliset romaanit.

Toinen bugi Huffmanin koodista löytyi demotilaisuudessa. Tämän olin jo aiemmin havainnut, mutta luulin korjanneeni sen. Bugi esiintyi silloin, kun interaktiivisessa käyttöliittymässä pakataan ja puretaan sama tiedosto useampaan otteeseen Huffmanin algoritmia käyttäen. Tällöin pakatun tiedoston koko hieman kasvoi suuremmaksi kuin edellinen, vaikka niiden pitäisi olla aina samankokoisia. Purkaminen kuitenkin tuotti oikean tuloksen. Mistään isommasta ongelmasta ei siis ollut kyse, vaan ongelma korjaantui yhdellä rivillä koodia. Bugi johtui siitä, että headerin luonnissa uusi header lisättiin vanhan perään, eli ratkaisuksi riitti tyhjentää header aina ennen uuden luontia.

Lisäksi taulukkoa on muutettu niin, että on myös omat sarakkeet tiedoston koolle ja pakatun tiedoston koolle. 
Testejä on lisätty ja päivitetty muutosten myötä. CompressionComparator-luokka oli aiemmin testien ulkopuolella, mutta nyt sille on tehty myös kattavat testit.


#### Tuntikirjanpito 

| Päivä       | Tuntimäärä  |
| ----------- | ----------- |
| 29.4.       | 2           |
| 2.5.        | 4,5         |
| 3.5         | 3           |
| 4.5.        | 1           |
| 7.5.        | 2           |
| 8.5.        | 3           |
| 9.5.        | 2,5         |
| 10.5.       | 7           |
| 11.5.       |             |
| Yhteensä    |    25       |



#### Tuntikirjanpito
Koko kurssiin käytetyt työtuntimäärät viikoittain.

| Viikko      | Tuntimäärä  |
| ----------- | ----------- |
| 1           | 5           |
| 2           | 22          |
| 3           | 21          |
| 4           | 19          |
| 5           | 22,5        |
| 6           | 30,5        |
| 7           |             |
| Yhteensä    |             |