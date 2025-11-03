# Struktura projektu Czech TV Program

```
ha_tv_program/
│
├── README.md                           # Hlavní dokumentace
├── info.md                             # HACS info
├── hacs.json                           # HACS konfigurace
├── examples.md                         # Příklady použití
├── install.sh                          # Instalační skript
│
├── custom_components/                  # Home Assistant integrace
│   └── cz_tv_program/
│       ├── __init__.py                 # Hlavní inicializační soubor
│       ├── manifest.json               # Manifest integrace
│       ├── const.py                    # Konstanty
│       ├── api.py                      # API klient pro ČT
│       ├── config_flow.py              # Konfigurace přes UI
│       ├── sensor.py                   # Senzory pro TV program
│       ├── strings.json                # Překlady (EN)
│       └── translations/
│           └── cs.json                 # České překlady
│
└── www/                                # Custom Lovelace karta
    └── tv-program-card.js              # TV Program Card

```

## Instalace do Home Assistant

### Ruční instalace

1. Zkopírujte `custom_components/cz_tv_program/` do `/config/custom_components/`
2. Zkopírujte `www/tv-program-card.js` do `/config/www/`
3. Restartujte Home Assistant
4. Přidejte integraci přes UI

### Automatická instalace

```bash
chmod +x install.sh
./install.sh
```

### HACS instalace

1. Přidejte jako custom repository v HACS
2. Nainstalujte integraci
3. Restartujte Home Assistant

## Soubory

### Integrace (custom_components/cz_tv_program/)

- **__init__.py** - Hlavní soubor integrace, nastavuje coordinator a platformy
- **manifest.json** - Metadata integrace (název, verze, závislosti)
- **const.py** - Konstanty (dostupné kanály, URL API, timeouty)
- **api.py** - API klient pro komunikaci s ČT API, parsování XML
- **config_flow.py** - Konfigurace přes UI (výběr kanálů)
- **sensor.py** - Vytváření sensorů pro každý kanál, atributy
- **strings.json** - Překlady pro UI
- **translations/cs.json** - České překlady

### Custom karta (www/)

- **tv-program-card.js** - Custom Lovelace karta pro zobrazení TV programu
  - Podporuje výběr počtu dní (1-7)
  - Zobrazuje aktuální pořad
  - Seznam nadcházejících pořadů
  - Konfigurovatelné zobrazení (žánr, délka, popis)

## Klíčové funkce

### API Client (api.py)
- Stahuje data z České televize XML API
- Respektuje rate limit (1 požadavek/minutu)
- Parsuje XML do strukturovaných dat
- Stahuje program na 7 dní dopředu

### Sensor (sensor.py)
- Vytváří senzor pro každý kanál
- State = aktuální pořad
- Atributy:
  - current_* - aktuální pořad
  - upcoming_programs - nadcházející pořady (10)
  - all_programs - kompletní týdenní program

### Custom Card (tv-program-card.js)
- Dynamické zobrazení programu
- Tlačítka pro výběr dní (1, 2, 3, 5, 7)
- Zvýraznění aktuálního pořadu
- Badgesy pro ŽIVĚ, PREMIÉRA
- Responzivní design

## API České televize

Oficiální dokumentace: https://www.ceskatelevize.cz/xml/tv-program/

### Endpoint
```
https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php
```

### Parametry
- `user` - uživatelské jméno (výchozí: "test")
- `date` - datum (formát: dd.mm.yyyy)
- `channel` - ID kanálu (ct1, ct2, ct24, ct4, ct5, ct6, ct7)
- `json=1` - volitelně pro JSON formát

### Dostupné kanály
- ct1 - ČT1
- ct2 - ČT2
- ct24 - ČT24
- ct4 - ČT sport
- ct5 - ČT :D
- ct6 - ČT art
- ct7 - ČT3

### Rate Limiting
- Maximum 1 požadavek za minutu
- Integrace respektuje tento limit pomocí sleep(1) mezi požadavky

## Technické detaily

### Dependencies
- aiohttp>=3.8.0
- Home Assistant >= 2023.1.0

### Update interval
- 6 hodin (SCAN_INTERVAL)

### Data storage
- Data jsou uložena v coordinator.data
- Formát: Dict[channel_id, List[program_dict]]

### Timezone
- Všechny časy jsou v lokálním timezone (Europe/Prague)

## Budoucí vylepšení

- [ ] Podpora dalších TV stanic (Prima, Nova)
- [ ] XMLTV format support
- [ ] Filtrování podle žánru
- [ ] Oblíbené pořady
- [ ] Notifikace před pořadem
- [ ] Vyhledávání v programu
- [ ] Export do kalendáře
