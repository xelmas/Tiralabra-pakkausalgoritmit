# Tiralabra-pakkausalgoritmit

Kurssi aineopintojen harjoitustyö: Algoritmit ja tekoäly.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/specification.md) \
[Testausdokumentaatio](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/testing.md) \
[Toteutusdokumentaatio](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/implementation.md) \
[Käyttöohje](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/user_manual.md)


## Viikkoraportit
[Viikkoraportti 1](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport1.md) \
[Viikkoraportti 2](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport2.md) \
[Viikkoraportti 3](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport3.md) \
[Viikkoraportti 4](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport4.md) \
[Viikkoraportti 5](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport5.md) \
[Viikkoraportti 6](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport6.md) \
[Viikkoraportti 7](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport7.md) 

## Asennusohjeet
1. Varmista, että poetry on asennettu komennolla ```poetry --version```
2. Kloonaa repositorio komennolla ```git clone```
3. Siirry hakemistoon ja asenna riippuvuudet komennolla ```poetry install```

## Komentorivitoiminnot

Sovellus voidaan käynnistää interaktiivisessa tai ei-interaktiivisessa versiossa.

### Sovelluksen käynnistys

#### Käynnistää sovelluksen interaktiivisen käyttöliittymän:
```
poetry run invoke start --function start
```

#### Käynnistää sovelluksen ja ajaa pakkaus- ja purkualgoritmin kaikille tiedostoille automaattisesti:
```
poetry run invoke start --function automatic_start
```

### Testien käynnistys

Testit voidaan ajaa joko kaikki kerralla tai valita suoritettavaksi joko yksikkötestit tai automaatiotestit.

#### Suorittaa yksikkötestit:
```
poetry run invoke unit-tests
```

#### Suorittaa automaatiotestit:
```
poetry run invoke automatic-tests
```

#### Suorittaa kaikki testit:
```
poetry run invoke test
```

#### Luo testikattavuusraportin kaikille testeille:
```
poetry run invoke coverage-report
```
### Muut komennot

#### Suorittaa pylint-tarkistuksen:
```
poetry run invoke lint
```
