# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-11-03

### Added
- ✨ Základní integrace pro stahování TV programu České televize
- 📺 Podpora všech 7 kanálů ČT (ČT1, ČT2, ČT24, ČT sport, ČT :D, ČT art, ČT3)
- 📅 Stahování týdenního programu dopředu
- 🎨 Custom Lovelace karta `tv-program-card`
- 🔧 Konfigurace přes UI s výběrem kanálů
- 🌍 České překlady
- 📊 Detailní atributy sensorů:
  - Aktuální pořad
  - Nadcházejících 10 pořadů
  - Kompletní týdenní program
- 🔄 Automatická aktualizace každých 6 hodin
- 📝 Kompletní dokumentace a příklady

### Features

#### Integrace
- Oficiální API České televize
- Rate limiting (1 požadavek/minutu)
- XML parsing s detailními informacemi
- Error handling a logging
- Config flow pro snadnou konfiguraci

#### Custom Karta
- Výběr zobrazení 1-7 dní
- Zvýraznění aktuálního pořadu
- Badgesy pro ŽIVĚ a PREMIÉRA
- Konfigurovatelné zobrazení žánru, délky a popisu
- Responzivní design
- Dark mode podpora

#### Dokumentace
- README s kompletním návodem
- Příklady konfigurace karet
- Příklady automatizací
- Instalační skript
- HACS kompatibilita

### Technical Details
- Home Assistant >= 2023.1.0
- Python async/await
- aiohttp pro HTTP požadavky
- XML parsing pomocí ElementTree
- Custom Lovelace card v vanilla JavaScript

---

## Plánované verze

### [1.1.0] - Plánováno
- 🔍 Vyhledávání v programu
- ⭐ Oblíbené pořady
- 🔔 Notifikace před začátkem pořadu
- 📱 Lepší mobilní zobrazení

### [1.2.0] - Plánováno
- 📺 Podpora dalších TV stanic (Prima, Nova)
- 🌐 XMLTV format support
- 🎯 Filtrování podle žánru
- 📅 Export do kalendáře

### [2.0.0] - Budoucnost
- 🤖 AI doporučení pořadů
- 📊 Statistiky sledovanosti
- 🎬 Integrace s TMDB/IMDb
- 🎮 Ovládání TV tuneru
