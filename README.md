# Tiralabra-pakkausalgoritmit

Kurssi aineopintojen harjoitustyö: Algoritmit ja tekoäly.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/specification.md) 

## Viikkoraportit
[Viikkoraportti 1](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport1.md) \
[Viikkoraportti 2](https://github.com/xelmas/Tiralabra-pakkausalgoritmit/blob/main/documentation/weeklyreports/weeklyreport2.md) 


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