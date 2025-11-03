#!/bin/bash

# Czech TV Program - Instalační skript pro Home Assistant
# =======================================================

echo "======================================"
echo "Czech TV Program - Instalace"
echo "======================================"
echo ""

# Detekce Home Assistant konfiguračního adresáře
if [ -d "/config" ]; then
    HA_CONFIG="/config"
elif [ -d "$HOME/.homeassistant" ]; then
    HA_CONFIG="$HOME/.homeassistant"
else
    echo "⚠️  Home Assistant konfigurační adresář nebyl nalezen!"
    read -p "Zadejte cestu k Home Assistant config adresáři: " HA_CONFIG
fi

echo "📁 Home Assistant config: $HA_CONFIG"
echo ""

# Vytvoření potřebných adresářů
echo "📂 Vytváření adresářů..."
mkdir -p "$HA_CONFIG/custom_components"
mkdir -p "$HA_CONFIG/www"

# Kontrola, zda existují zdrojové soubory
if [ ! -d "custom_components/cz_tv_program" ]; then
    echo "❌ Chyba: Složka custom_components/cz_tv_program nebyla nalezena!"
    echo "   Spusťte tento skript ze složky projektu."
    exit 1
fi

# Kopírování integrace
echo "📦 Kopírování integrace..."
if [ -d "$HA_CONFIG/custom_components/cz_tv_program" ]; then
    echo "⚠️  Integrace již existuje. Přepsat? (ano/ne)"
    read -r RESPONSE
    if [ "$RESPONSE" != "ano" ] && [ "$RESPONSE" != "a" ] && [ "$RESPONSE" != "y" ] && [ "$RESPONSE" != "yes" ]; then
        echo "   Přeskakuji instalaci integrace..."
    else
        rm -rf "$HA_CONFIG/custom_components/cz_tv_program"
        cp -r "custom_components/cz_tv_program" "$HA_CONFIG/custom_components/"
        echo "✅ Integrace aktualizována"
    fi
else
    cp -r "custom_components/cz_tv_program" "$HA_CONFIG/custom_components/"
    echo "✅ Integrace nainstalována"
fi

# Kopírování karty
echo "🎨 Kopírování custom karty..."
if [ -f "$HA_CONFIG/www/tv-program-card.js" ]; then
    echo "⚠️  Karta již existuje. Přepsat? (ano/ne)"
    read -r RESPONSE
    if [ "$RESPONSE" != "ano" ] && [ "$RESPONSE" != "a" ] && [ "$RESPONSE" != "y" ] && [ "$RESPONSE" != "yes" ]; then
        echo "   Přeskakuji instalaci karty..."
    else
        cp "www/tv-program-card.js" "$HA_CONFIG/www/"
        echo "✅ Karta aktualizována"
    fi
else
    cp "www/tv-program-card.js" "$HA_CONFIG/www/"
    echo "✅ Karta nainstalována"
fi

echo ""
echo "======================================"
echo "✨ Instalace dokončena!"
echo "======================================"
echo ""
echo "📝 Další kroky:"
echo ""
echo "1. Restartujte Home Assistant"
echo ""
echo "2. Přidejte resource pro custom kartu:"
echo "   Nastavení → Dashboardy → Resources → Add Resource"
echo "   URL: /local/tv-program-card.js"
echo "   Type: JavaScript Module"
echo ""
echo "3. Přidejte integraci:"
echo "   Nastavení → Zařízení a služby → + Přidat integraci"
echo "   Vyhledejte: Czech TV Program"
echo ""
echo "4. Přidejte kartu do dashboardu:"
echo "   Upravit dashboard → + Add Card"
echo "   Vyhledejte: TV Program Card"
echo ""
echo "📖 Pro více informací viz README.md"
echo ""
