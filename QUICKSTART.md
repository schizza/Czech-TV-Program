# 🚀 Rychlý start - Czech TV Program

## 📥 Stažení a instalace

1. **Stáhněte ZIP soubor** `cz_tv_program.zip`
2. **Rozbalte** obsah archivu
3. **Spusťte instalaci** jedním z následujících způsobů:

---

## ⚡ Automatická instalace (doporučeno)

### Linux / macOS
```bash
cd ha_tv_program
chmod +x install.sh
./install.sh
```

### Windows (PowerShell)
```powershell
cd ha_tv_program
# Ručně zkopírujte složky podle instrukcí níže
```

---

## 📁 Ruční instalace

### Krok 1: Zkopírujte integraci
```
ha_tv_program/custom_components/cz_tv_program/
    ↓ zkopírovat do ↓
/config/custom_components/cz_tv_program/
```

### Krok 2: Zkopírujte kartu
```
ha_tv_program/www/tv-program-card.js
    ↓ zkopírovat do ↓
/config/www/tv-program-card.js
```

### Krok 3: Restartujte Home Assistant
- **Nastavení** → **Systém** → **Restartovat**

---

## 🎨 Konfigurace

### 1. Přidejte integraci
1. **Nastavení** → **Zařízení a služby**
2. Klikněte **+ Přidat integraci**
3. Vyhledejte **"Czech TV Program"**
4. Vyberte TV kanály:
   - ✅ ČT1
   - ✅ ČT2
   - ✅ ČT24
   - ✅ ČT sport
   - ✅ ČT :D
   - ✅ ČT art
   - ✅ ČT3
5. Klikněte **Odeslat**

### 2. Přidejte kartu jako resource
1. **Nastavení** → **Dashboardy**
2. Klikněte na **⋮** (tři tečky) → **Resources**
3. Klikněte **+ Add Resource**
4. Vyplňte:
   - **URL:** `/local/tv-program-card.js`
   - **Resource type:** `JavaScript Module`
5. Klikněte **Create**
6. **Obnovte stránku** (Ctrl+F5 nebo Cmd+R)

### 3. Přidejte kartu do dashboardu
1. Otevřete váš dashboard
2. Klikněte **✏️ Edit Dashboard**
3. Klikněte **+ Add Card**
4. V dolní části najděte **"TV Program Card"**
5. Nebo použijte manuální konfiguraci:
   ```yaml
   type: custom:tv-program-card
   entity: sensor.tv_program_ct1
   title: Program ČT1
   days: 3
   ```
6. Klikněte **Save**

---

## ✅ Kontrola funkčnosti

Po instalaci byste měli vidět:

### Senzory (automaticky vytvořené)
- `sensor.tv_program_ct1`
- `sensor.tv_program_ct2`
- `sensor.tv_program_ct24`
- atd.

### State senzoru
```
"Aktuální název pořadu"
```

### Atributy senzoru
```yaml
current_title: "Události"
current_time: "19:00"
current_genre: "Zpravodajství"
upcoming_programs:
  - title: "Sportovní noviny"
    time: "19:30"
  - title: "Počasí"
    time: "19:45"
```

---

## 🎯 První karta - Příklad

Nejjednodušší konfigurace:

```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct1
```

Pokročilá konfigurace:

```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct1
title: "📺 Program ČT1"
days: 5
show_genre: true
show_duration: true
show_description: true
```

---

## 🐛 Řešení problémů

### ❌ Karta se nezobrazuje
**Řešení:**
1. Zkontrolujte, že je soubor `tv-program-card.js` ve složce `/config/www/`
2. Ověřte, že je resource přidán v dashboardu
3. Obnovte stránku s vymazáním cache: **Ctrl+F5** (Windows) nebo **Cmd+Shift+R** (Mac)
4. Zkontrolujte browser console (F12) pro chyby

### ❌ Integrace se nenačte
**Řešení:**
1. Ověřte, že složka je správně umístěna:
   `/config/custom_components/cz_tv_program/`
2. Restartujte Home Assistant
3. Zkontrolujte logy: **Nastavení** → **Systém** → **Logy**
4. Hledejte chyby obsahující `cz_tv_program`

### ❌ Data se neaktualizují
**Řešení:**
1. Zkontrolujte internetové připojení
2. API České televize může být dočasně nedostupné
3. Zkontrolujte logy pro chyby HTTP
4. Počkejte 6 hodin (automatická aktualizace)

### ❌ "Entity not found"
**Řešení:**
1. Ujistěte se, že integrace je přidána
2. Zkontrolujte, že vybraný kanál je v konfiguraci
3. Restartujte Home Assistant
4. Zkontrolujte správný název entity v **Developer Tools** → **States**

---

## 📚 Další materiály

- **README.md** - Kompletní dokumentace
- **examples.md** - Příklady karet a automatizací
- **STRUCTURE.md** - Technická dokumentace

---

## 🆘 Podpora

**Nenašli jste řešení?**
- Zkontrolujte dokumentaci v README.md
- Podívejte se na příklady v examples.md
- Zkontrolujte logy Home Assistantu

---

**Užijte si sledování TV programu! 📺✨**
