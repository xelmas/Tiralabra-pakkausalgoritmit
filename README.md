# Tiralabra-pakkausalgoritmit

Kurssi aineopintojen harjoitustyö: Algoritmit ja tekoäly.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/specification.md) \
[Testausdokumentaatio](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/testing.md) \
[Toteutusdokumentaatio](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/implementation.md)

## Viikkoraportit
[Viikkoraportti 1](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport1.md) \
[Viikkoraportti 2](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport2.md) \
[Viikkoraportti 3](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport3.md) \
[Viikkoraportti 4](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport4.md) 

## Asennusohjeet
1. Varmista, että poetry on asennettu komennolla ```poetry --version```
2. Kloonaa repositorio komennolla ```git clone```
3. Siirry hakemistoon ja asenna riippuvuudet komennolla ```poetry install```

## Komentorivitoiminnot

### Käynnistää sovelluksen:
```
poetry run invoke start
```

### Suorittaa pylint-tarkistuksen:
```
poetry run invoke lint
```

### Suorittaa testit:
```
poetry run invoke test
```

### Luo testikattavuusraportin:
```
poetry run invoke coverage-report
```