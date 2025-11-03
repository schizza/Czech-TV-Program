# Ukázkové konfigurace pro TV Program Card

## Příklad 1: Základní karta s jedním kanálem
```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct1
title: Program ČT1
days: 3
```

## Příklad 2: Kompaktní zobrazení bez popisů
```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct24
title: ČT24 Zprávy
days: 1
show_description: false
max_programs: 20
```

## Příklad 3: Detailní zobrazení na týden
```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct1
title: Týdenní program ČT1
days: 7
show_genre: true
show_duration: true
show_description: true
max_programs: 100
```

## Příklad 4: Více karet v jednom view
```yaml
type: vertical-stack
cards:
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct1
    title: ČT1
    days: 2
    
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct2
    title: ČT2
    days: 2
    
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct24
    title: ČT24
    days: 2
```

## Příklad 5: Grid layout s několika kanály
```yaml
type: grid
columns: 2
square: false
cards:
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct1
    title: ČT1
    days: 3
    show_description: false
    
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct2
    title: ČT2
    days: 3
    show_description: false
    
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct24
    title: ČT24
    days: 3
    show_description: false
    
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct4
    title: ČT sport
    days: 3
    show_description: false
```

## Příklad 6: Kombinace s entity card
```yaml
type: vertical-stack
cards:
  # Přehled aktuálních pořadů
  - type: entities
    title: Nyní na obrazovkách
    entities:
      - entity: sensor.tv_program_ct1
        name: ČT1
        icon: mdi:television-classic
      - entity: sensor.tv_program_ct2
        name: ČT2
        icon: mdi:television-classic
      - entity: sensor.tv_program_ct24
        name: ČT24
        icon: mdi:television-classic
  
  # Detailní program vybraného kanálu
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct1
    title: Detailní program ČT1
    days: 5
```

## Příklad 7: Použití conditional card (zobrazit pouze když běží film)
```yaml
type: conditional
conditions:
  - entity: sensor.tv_program_ct1
    state_not: "Nedostupné"
  - condition: template
    value_template: "{{ 'Film' in state_attr('sensor.tv_program_ct1', 'current_genre') }}"
card:
  type: custom:tv-program-card
  entity: sensor.tv_program_ct1
  title: "🎬 Film na ČT1"
  days: 1
```

## Příklad 8: Sportovní kanály s custom nadpisem
```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      # 🏆 Sportovní program
      
  - type: custom:tv-program-card
    entity: sensor.tv_program_ct4
    title: ČT sport
    days: 3
```

## Příklad 9: Pro děti - dětský program
```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct5
title: "🎨 Program pro děti - ČT :D"
days: 3
show_genre: true
show_duration: true
```

## Příklad 10: Minimalistické zobrazení
```yaml
type: custom:tv-program-card
entity: sensor.tv_program_ct24
title: ČT24
days: 1
show_genre: false
show_duration: false
show_description: false
max_programs: 10
```

## Automatizace - Příklady použití

### Notifikace před začátkem oblíbeného pořadu
```yaml
automation:
  - alias: "Upozornění na Večerníček"
    trigger:
      - platform: time
        at: "18:45:00"
    condition:
      - condition: template
        value_template: >
          {% set upcoming = state_attr('sensor.tv_program_ct1', 'upcoming_programs') %}
          {{ upcoming and 'Večerníček' in upcoming[0].title }}
    action:
      - service: notify.mobile_app
        data:
          title: "📺 TV Upozornění"
          message: "Za 15 minut začíná Večerníček na ČT1!"
```

### Notifikace když běží sport
```yaml
automation:
  - alias: "Sport na ČT sport"
    trigger:
      - platform: state
        entity_id: sensor.tv_program_ct4
    condition:
      - condition: template
        value_template: "{{ 'fotbal' in state_attr('sensor.tv_program_ct4', 'current_title')|lower }}"
    action:
      - service: notify.home
        data:
          message: "⚽ Fotbal právě začal na ČT sport!"
```

### Zapnutí TV když začíná zpravodajství
```yaml
automation:
  - alias: "Automatické zapnutí TV na zprávy"
    trigger:
      - platform: time
        at: "19:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.doma
        state: "on"
      - condition: template
        value_template: "{{ 'Události' in state_attr('sensor.tv_program_ct1', 'current_title') }}"
    action:
      - service: media_player.turn_on
        target:
          entity_id: media_player.televize
      - service: media_player.select_source
        target:
          entity_id: media_player.televize
        data:
          source: "ČT1"
```

### Denní přehled zajímavých pořadů
```yaml
automation:
  - alias: "Ranní přehled TV programu"
    trigger:
      - platform: time
        at: "07:00:00"
    action:
      - service: notify.mobile_app
        data:
          title: "📺 Dnešní TV program"
          message: >
            ČT1: {{ state_attr('sensor.tv_program_ct1', 'current_title') }}
            ČT2: {{ state_attr('sensor.tv_program_ct2', 'current_title') }}
            ČT24: {{ state_attr('sensor.tv_program_ct24', 'current_title') }}
```

## Šablony (Templates)

### V kartě s markdown zobrazit aktuální pořad
```yaml
type: markdown
content: |
  ## 📺 Nyní v televizi
  
  **ČT1:** {{ state_attr('sensor.tv_program_ct1', 'current_title') }}  
  *{{ state_attr('sensor.tv_program_ct1', 'current_time') }} - {{ state_attr('sensor.tv_program_ct1', 'current_genre') }}*
  
  **ČT24:** {{ state_attr('sensor.tv_program_ct24', 'current_title') }}  
  *{{ state_attr('sensor.tv_program_ct24', 'current_time') }} - zpravodajství*
```

### Zjistit čas dalšího pořadu
```jinja2
{% set upcoming = state_attr('sensor.tv_program_ct1', 'upcoming_programs') %}
{% if upcoming %}
  Další pořad: {{ upcoming[0].title }} v {{ upcoming[0].time }}
{% endif %}
```

### Vyhledat filmy v programu
```jinja2
{% set all_programs = state_attr('sensor.tv_program_ct1', 'all_programs') %}
{% set movies = all_programs | selectattr('genre', 'eq', 'Film') | list %}
Počet filmů dnes: {{ movies | length }}
```
