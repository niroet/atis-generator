// ============================================================================
// ATIS SCHEMA REFERENCE
// A comprehensive guide to the data model and generation system
// ============================================================================

#import "@preview/cetz:0.3.2": canvas, draw

// ============================================================================
// THEME & CONFIGURATION
// ============================================================================

#let primary = rgb("#0891b2")      // Cyan - primary, aviation feel
#let secondary = rgb("#6366f1")    // Indigo - reference data
#let success = rgb("#10b981")      // Emerald - good conditions
#let warning = rgb("#f59e0b")      // Amber - caution
#let danger = rgb("#ef4444")       // Red - critical/hard
#let neutral = rgb("#475569")      // Slate - neutral text

#let bg-light = rgb("#f8fafc")
#let bg-code = rgb("#1e293b")
#let border-light = rgb("#e2e8f0")

// ============================================================================
// DOCUMENT SETUP
// ============================================================================

#set document(title: "ATIS Schema Reference", author: "Aevoli")
#set page(
  margin: (x: 2.5cm, y: 2cm),
  numbering: "1 / 1",
  number-align: right,
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 9pt, fill: neutral)
      #grid(
        columns: (1fr, 1fr),
        align(left)[ATIS Schema Reference],
        align(right)[Aevoli Pilot Training]
      )
      #v(-0.5em)
      #line(length: 100%, stroke: 0.5pt + border-light)
    ]
  }
)

#set text(size: 10pt, fill: rgb("#1e293b"))
#set par(justify: true, leading: 0.65em)
#set heading(numbering: none)

// Heading styles
#show heading.where(level: 1): it => {
  v(1.5em)
  text(size: 18pt, weight: "bold", fill: primary)[#it.body]
  v(0.3em)
  line(length: 100%, stroke: 2pt + primary)
  v(0.8em)
}

#show heading.where(level: 2): it => {
  v(1.2em)
  text(size: 14pt, weight: "bold", fill: neutral)[#it.body]
  v(0.5em)
}

#show heading.where(level: 3): it => {
  v(0.8em)
  text(size: 11pt, weight: "bold", fill: neutral)[#it.body]
  v(0.3em)
}

// Code block styling
#show raw.where(block: true): it => {
  set text(size: 9pt)
  block(
    width: 100%,
    fill: bg-code,
    inset: 12pt,
    radius: 6pt,
  )[#text(fill: rgb("#e2e8f0"))[#it]]
}

#show raw.where(block: false): it => {
  box(
    fill: bg-light,
    inset: (x: 4pt, y: 2pt),
    radius: 3pt,
  )[#text(size: 9pt, fill: primary)[#it]]
}

// ============================================================================
// CUSTOM COMPONENTS
// ============================================================================

// Entity card
#let entity(name, color: primary, icon: "●", fields) = {
  block(
    width: 100%,
    stroke: 1.5pt + color,
    radius: 8pt,
    clip: true,
  )[
    #block(
      width: 100%,
      fill: color,
      inset: 10pt,
    )[
      #text(fill: white, weight: "bold", size: 11pt)[#icon #name]
    ]
    #block(
      width: 100%,
      fill: white,
      inset: 10pt,
    )[
      #set text(size: 9pt)
      #fields
    ]
  ]
}

// Callout box
#let callout(title, body, color: primary, icon: "ℹ") = {
  block(
    width: 100%,
    fill: color.lighten(90%),
    stroke: (left: 3pt + color),
    inset: 12pt,
    radius: (right: 6pt),
  )[
    #text(weight: "bold", fill: color)[#icon #title]
    #v(0.3em)
    #body
  ]
}

// Difficulty badge
#let difficulty-badge(level) = {
  let colors = (
    "super_easy": success,
    "easy": rgb("#22c55e"),
    "medium": warning,
    "hard": danger,
  )
  let labels = (
    "super_easy": "SUPER EASY",
    "easy": "EASY",
    "medium": "MEDIUM", 
    "hard": "HARD",
  )
  let color = colors.at(level, default: neutral)
  box(
    fill: color.lighten(80%),
    stroke: 1pt + color,
    inset: (x: 8pt, y: 3pt),
    radius: 12pt,
  )[#text(size: 8pt, fill: color, weight: "bold")[#labels.at(level, default: level)]]
}

// Weather code badge
#let wx-code(code) = {
  box(
    fill: bg-light,
    stroke: 0.5pt + border-light,
    inset: (x: 6pt, y: 2pt),
    radius: 4pt,
  )[#text(size: 9pt, font: "Consolas", fill: neutral)[#code]]
}

// Meter/range indicator
#let range-indicator(label, min, max, unit: "", color: primary) = {
  block(
    fill: color.lighten(92%),
    stroke: 1pt + color.lighten(50%),
    radius: 6pt,
    inset: 8pt,
    width: 100%,
  )[
    #text(size: 8pt, fill: neutral)[#label]
    #v(2pt)
    #text(size: 11pt, weight: "bold", fill: color)[#min #sym.dash.en #max#unit]
  ]
}

// ============================================================================
// TITLE PAGE
// ============================================================================

#v(3cm)

#align(center)[
  #block(
    width: 80%,
    inset: 2em,
  )[
    #text(size: 36pt, weight: "bold", fill: primary)[ATIS]
    #v(-0.3em)
    #text(size: 36pt, weight: "bold", fill: neutral)[Schema Reference]
    
    #v(1.5em)
    
    #text(size: 14pt, fill: neutral)[
      Automatic Terminal Information Service \
      Data Model & Generation System
    ]
    
    #v(2em)
    
    #line(length: 40%, stroke: 2pt + border-light)
    
    #v(2em)
    
    #grid(
      columns: 3,
      gutter: 2em,
      align: center,
      [
        #text(size: 24pt, weight: "bold", fill: primary)[37]
        #v(-0.5em)
        #text(size: 10pt, fill: neutral)[DACH Airports]
      ],
      [
        #text(size: 24pt, weight: "bold", fill: secondary)[4]
        #v(-0.5em)
        #text(size: 10pt, fill: neutral)[Difficulty Tiers]
      ],
      [
        #text(size: 24pt, weight: "bold", fill: success)[500]
        #v(-0.5em)
        #text(size: 10pt, fill: neutral)[ATIS Entries]
      ],
    )
  ]
]

#v(1fr)

#align(center)[
  #text(fill: neutral)[Aevoli Pilot Training Platform]
  #v(0.3em)
  #text(size: 9pt, fill: neutral.lighten(30%))[Version 1.0 · January 2026]
]

#pagebreak()

// ============================================================================
// TABLE OF CONTENTS
// ============================================================================

#outline(
  title: [Contents],
  indent: 1.5em,
  depth: 2,
)

#pagebreak()

// ============================================================================
// SECTION 1: WHAT IS ATIS?
// ============================================================================

= What is ATIS?

ATIS (Automatic Terminal Information Service) is a continuous broadcast of recorded aeronautical information at busy airports. Pilots listen to ATIS before contacting ATC to get essential information about weather, active runways, and operational notices.

== Real-World ATIS Structure

#callout(
  "Key Concept",
  [Every ATIS broadcast follows a standardized format. Understanding this structure is essential for quick and accurate comprehension during high-workload phases of flight.],
  color: primary,
  icon: "📻"
)

#v(1em)

#align(center)[
  #block(
    width: 90%,
    fill: bg-light,
    stroke: 1pt + border-light,
    radius: 8pt,
    inset: 1.5em,
  )[
    #set text(size: 10pt)
    #set par(leading: 0.8em)
    
    #text(weight: "bold", fill: primary)[Frankfurt Information #text(fill: danger)[Alpha]] \
    #v(0.3em)
    #text(fill: neutral)[
      Recorded at #text(weight: "bold")[1350 Zulu] \
      Runway in use #text(weight: "bold")[25L] for landing, #text(weight: "bold")[25C] for takeoff \
      ILS approach \
      Transition level #text(weight: "bold")[70] \
      #v(0.5em)
      Wind #text(weight: "bold")[240 degrees 12 knots] \
      Visibility #text(weight: "bold")[10 kilometers or more] \
      Few clouds #text(weight: "bold")[3000 feet], scattered #text(weight: "bold")[8000 feet] \
      Temperature #text(weight: "bold")[18], dewpoint #text(weight: "bold")[12] \
      QNH #text(weight: "bold")[1018] \
      #v(0.5em)
      #text(style: "italic")[Acknowledge receipt of information Alpha]
    ]
  ]
]

#v(1em)

== Components of an ATIS

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  
  [
    === Identification
    - Airport name
    - Information letter (Alpha–Zulu)
    - Recording time (Zulu)
    
    === Runway Information
    - Active runway(s)
    - Approach type (ILS, RNAV, etc.)
    - Transition level
  ],
  
  [
    === Weather
    - Wind (direction, speed, gusts)
    - Visibility (meters/km)
    - Weather phenomena (rain, fog, etc.)
    - Clouds (type, height, CB)
    - Temperature & dewpoint
    - QNH (altimeter setting)
    
    === Remarks
    - Operational notices
    - Hazards
    - NOTAMs
  ]
)

#pagebreak()

// ============================================================================
// SECTION 2: DATA MODEL
// ============================================================================

= Data Model

The ATIS system uses two main collections in Directus, with a clean relational structure.

== Schema Overview

#align(center)[
  #canvas(length: 1cm, {
    import draw: *
    
    // Airport box
    rect((-2, 2), (2, 4), fill: success.lighten(85%), stroke: 2pt + success, radius: 0.3)
    content((0, 3.4), text(weight: "bold", size: 12pt, fill: success)[airport])
    content((0, 2.6), text(size: 8pt, fill: neutral)[37 DACH airports])
    
    // ATIS entries box
    rect((5, 1), (11, 5), fill: primary.lighten(85%), stroke: 2pt + primary, radius: 0.3)
    content((8, 4.3), text(weight: "bold", size: 12pt, fill: primary)[atis_entries])
    content((8, 3.5), text(size: 8pt, fill: neutral)[Generated practice ATIS])
    
    // Fields preview
    content((8, 2.8), text(size: 7pt, fill: neutral)[information_letter])
    content((8, 2.4), text(size: 7pt, fill: neutral)[wind, visibility, clouds])
    content((8, 2.0), text(size: 7pt, fill: neutral)[runway, qnh, temp...])
    content((8, 1.5), text(size: 7pt, fill: neutral)[difficulty, full_text])
    
    // Relation arrow
    line((2, 3), (5, 3), stroke: 1.5pt + neutral, mark: (end: ">"))
    content((3.5, 3.5), text(size: 8pt, fill: neutral)[M:1])
    content((3.5, 2.5), text(size: 7pt, style: "italic", fill: neutral)[airport])
  })
]

#v(1em)

== Collections

#grid(
  columns: (1fr, 1fr),
  gutter: 1.5em,
  
  entity("airport", color: success, icon: "✈", [
    Shared reference collection for all tools
    #v(0.5em)
    #table(
      columns: (auto, 1fr),
      stroke: none,
      inset: 3pt,
      [`icao`], [4-letter ICAO code (EDDF, LOWW...)],
      [`name`], [Full airport name],
      [`city`], [City name],
      [`country`], [DE, AT, or CH],
      [`elevation_ft`], [Field elevation in feet],
      [`transition_altitude`], [TA in feet (usually 5000)],
      [`runways`], [JSON array of runway configs],
    )
  ]),
  
  entity("atis_entries", color: primary, icon: "📻", [
    Generated ATIS broadcasts for practice
    #v(0.5em)
    *Core fields:*
    - `airport` → linked airport
    - `information_letter` (Alpha–Zulu)
    - `observation_time`
    - `difficulty`
    - `full_text` (spoken ATIS)
    
    *See next page for full field list*
  ]),
)

#pagebreak()

== ATIS Entry Fields

The `atis_entries` collection contains all components of an ATIS broadcast:

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  
  [
    === Identification
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`information_letter`], [Alpha, Bravo, Charlie...],
      [`observation_time`], [Recording time (Zulu)],
      [`difficulty`], [super_easy → hard],
    )
    
    === Runway
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`runway_in_use`], [Active runway designator],
      [`approach_type`], [ILS, RNAV, Visual...],
      [`transition_level`], [FL for transition],
    )
    
    === Temperature & Pressure
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`temperature`], [°C],
      [`dewpoint`], [°C],
      [`qnh`], [hPa],
    )
  ],
  
  [
    === Wind
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`wind_direction`], [Degrees (0–360)],
      [`wind_speed`], [Knots],
      [`wind_gust`], [Gust speed (if any)],
      [`wind_variable_from`], [Variable range start],
      [`wind_variable_to`], [Variable range end],
      [`is_calm`], [Calm wind flag],
    )
    
    === Visibility & Clouds
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`visibility`], [Meters (9999 = 10km+)],
      [`rvr`], [JSON: runway visual range],
      [`weather`], [JSON: phenomena codes],
      [`clouds`], [JSON: cloud layers],
      [`is_cavok`], [CAVOK flag],
    )
    
    === Output
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 6pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Field*], [*Description*],
      [`full_text`], [Complete spoken ATIS],
      [`remarks`], [JSON: operational notes],
    )
  ],
)

#pagebreak()

// ============================================================================
// SECTION 3: DIFFICULTY SYSTEM
// ============================================================================

= Difficulty System

The 4-tier difficulty system provides a progressive learning path from beginner to professional readiness.

== Tier Overview

#v(0.5em)

#grid(
  columns: 2,
  gutter: 1em,
  
  block(
    width: 100%,
    stroke: 2pt + success,
    radius: 10pt,
    clip: true,
  )[
    #block(fill: success, width: 100%, inset: 10pt)[
      #text(fill: white, weight: "bold", size: 12pt)[① SUPER EASY]
    ]
    #block(inset: 12pt)[
      #text(size: 9pt, style: "italic", fill: neutral)[
        "Perfect weather, simple format — for learning ATIS structure"
      ]
      #v(0.5em)
      
      #grid(columns: 2, gutter: 0.5em,
        range-indicator("Visibility", "10", "km+", color: success),
        range-indicator("Wind", "0", "8 kt", color: success),
      )
      #v(0.5em)
      
      - CAVOK 70% probability
      - No gusts, no weather
      - Single runway only
      - Round numbers (QNH: 1013, 1020)
      - No remarks
    ]
  ],
  
  block(
    width: 100%,
    stroke: 2pt + rgb("#22c55e"),
    radius: 10pt,
    clip: true,
  )[
    #block(fill: rgb("#22c55e"), width: 100%, inset: 10pt)[
      #text(fill: white, weight: "bold", size: 12pt)[② EASY]
    ]
    #block(inset: 12pt)[
      #text(size: 9pt, style: "italic", fill: neutral)[
        "Good weather with minor variations — building confidence"
      ]
      #v(0.5em)
      
      #grid(columns: 2, gutter: 0.5em,
        range-indicator("Visibility", "5", "10 km", color: rgb("#22c55e")),
        range-indicator("Wind", "3", "15 kt", color: rgb("#22c55e")),
      )
      #v(0.5em)
      
      - CAVOK 30% probability
      - Rare gusts (5%)
      - Light weather only: #wx-code("-RA") #wx-code("-DZ") #wx-code("BR")
      - Max 1 remark
      - Still uses round numbers
    ]
  ],
  
  block(
    width: 100%,
    stroke: 2pt + warning,
    radius: 10pt,
    clip: true,
  )[
    #block(fill: warning, width: 100%, inset: 10pt)[
      #text(fill: white, weight: "bold", size: 12pt)[③ MEDIUM]
    ]
    #block(inset: 12pt)[
      #text(size: 9pt, style: "italic", fill: neutral)[
        "Realistic operational conditions — developing proficiency"
      ]
      #v(0.5em)
      
      #grid(columns: 2, gutter: 0.5em,
        range-indicator("Visibility", "1.5", "10 km", color: warning),
        range-indicator("Wind", "5", "28 kt", color: warning),
      )
      #v(0.5em)
      
      - Gusts 25% probability
      - Variable winds possible
      - RVR when visibility low
      - Multiple cloud layers
      - Weather: #wx-code("RA") #wx-code("SN") #wx-code("SHRA") #wx-code("HZ")
      - Max 2 remarks
    ]
  ],
  
  block(
    width: 100%,
    stroke: 2pt + danger,
    radius: 10pt,
    clip: true,
  )[
    #block(fill: danger, width: 100%, inset: 10pt)[
      #text(fill: white, weight: "bold", size: 12pt)[④ HARD]
    ]
    #block(inset: 12pt)[
      #text(size: 9pt, style: "italic", fill: neutral)[
        "Challenging weather — professional readiness"
      ]
      #v(0.5em)
      
      #grid(columns: 2, gutter: 0.5em,
        range-indicator("Visibility", "100m", "5 km", color: danger),
        range-indicator("Wind", "8", "45 kt", color: danger),
      )
      #v(0.5em)
      
      - Gusts 50% probability
      - RVR 60% probability
      - Cumulonimbus clouds
      - Wind shear possible
      - All weather types
      - Up to 4 cloud layers
      - Max 3 complex remarks
    ]
  ],
)

#pagebreak()

== Parameter Comparison

#table(
  columns: (2fr, 1fr, 1fr, 1fr, 1fr),
  stroke: 0.5pt + border-light,
  inset: 8pt,
  fill: (col, row) => {
    if row == 0 { bg-light }
    else if col == 1 { success.lighten(90%) }
    else if col == 2 { rgb("#22c55e").lighten(90%) }
    else if col == 3 { warning.lighten(90%) }
    else if col == 4 { danger.lighten(90%) }
    else { white }
  },
  
  [*Parameter*], 
  [#difficulty-badge("super_easy")], 
  [#difficulty-badge("easy")], 
  [#difficulty-badge("medium")], 
  [#difficulty-badge("hard")],
  
  [Min visibility], [10 km], [5 km], [1.5 km], [100 m],
  [Max wind], [8 kt], [15 kt], [28 kt], [45 kt],
  [Gust probability], [0%], [5%], [25%], [50%],
  [CAVOK probability], [70%], [30%], [15%], [0%],
  [Weather probability], [0%], [15%], [40%], [75%],
  [Max cloud layers], [1], [2], [3], [4],
  [Min ceiling], [5000 ft], [3000 ft], [800 ft], [100 ft],
  [RVR probability], [0%], [0%], [20%], [60%],
  [Variable wind prob], [0%], [10%], [25%], [35%],
  [Max remarks], [0], [1], [2], [3],
  [Round numbers], [Yes], [Yes], [No], [No],
  [CB probability], [0%], [0%], [0%], [15%],
)

#pagebreak()

// ============================================================================
// SECTION 4: WEATHER CODES
// ============================================================================

= Weather Codes

ATIS uses standardized ICAO weather codes. The generator produces realistic combinations based on difficulty.

== Weather Phenomena

#grid(
  columns: (1fr, 1fr),
  gutter: 1.5em,
  
  [
    === Intensity Prefixes
    #table(
      columns: (auto, 1fr, auto),
      stroke: 0.5pt + border-light,
      inset: 8pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Code*], [*Meaning*], [*Example*],
      [#wx-code("-")], [Light], [#wx-code("-RA")],
      [(none)], [Moderate], [#wx-code("RA")],
      [#wx-code("+")], [Heavy], [#wx-code("+RA")],
    )
    
    === Precipitation
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 8pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Code*], [*Meaning*],
      [#wx-code("RA")], [Rain],
      [#wx-code("SN")], [Snow],
      [#wx-code("DZ")], [Drizzle],
      [#wx-code("SG")], [Snow grains],
      [#wx-code("GR")], [Hail],
      [#wx-code("GS")], [Small hail],
      [#wx-code("PL")], [Ice pellets],
    )
  ],
  
  [
    === Obscuration
    #table(
      columns: (auto, 1fr),
      stroke: 0.5pt + border-light,
      inset: 8pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Code*], [*Meaning*],
      [#wx-code("BR")], [Mist (vis 1–5 km)],
      [#wx-code("FG")], [Fog (vis < 1 km)],
      [#wx-code("HZ")], [Haze],
      [#wx-code("FU")], [Smoke],
    )
    
    === Descriptors
    #table(
      columns: (auto, 1fr, auto),
      stroke: 0.5pt + border-light,
      inset: 8pt,
      fill: (_, row) => if row == 0 { bg-light } else { white },
      [*Code*], [*Meaning*], [*Example*],
      [#wx-code("SH")], [Showers], [#wx-code("SHRA")],
      [#wx-code("TS")], [Thunderstorm], [#wx-code("TSRA")],
      [#wx-code("FZ")], [Freezing], [#wx-code("FZRA")],
      [#wx-code("BL")], [Blowing], [#wx-code("BLSN")],
    )
  ],
)

#v(1em)

== Cloud Types

#grid(
  columns: 4,
  gutter: 1em,
  
  block(fill: success.lighten(90%), stroke: 1pt + success, radius: 6pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(weight: "bold", fill: success)[FEW]
      #v(0.3em)
      #text(size: 9pt)[1–2 oktas]
      #v(0.2em)
      #text(size: 8pt, fill: neutral)[Few clouds]
    ]
  ],
  
  block(fill: rgb("#22c55e").lighten(90%), stroke: 1pt + rgb("#22c55e"), radius: 6pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(weight: "bold", fill: rgb("#22c55e"))[SCT]
      #v(0.3em)
      #text(size: 9pt)[3–4 oktas]
      #v(0.2em)
      #text(size: 8pt, fill: neutral)[Scattered]
    ]
  ],
  
  block(fill: warning.lighten(90%), stroke: 1pt + warning, radius: 6pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(weight: "bold", fill: warning)[BKN]
      #v(0.3em)
      #text(size: 9pt)[5–7 oktas]
      #v(0.2em)
      #text(size: 8pt, fill: neutral)[Broken]
    ]
  ],
  
  block(fill: danger.lighten(90%), stroke: 1pt + danger, radius: 6pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(weight: "bold", fill: danger)[OVC]
      #v(0.3em)
      #text(size: 9pt)[8 oktas]
      #v(0.2em)
      #text(size: 8pt, fill: neutral)[Overcast]
    ]
  ],
)

#v(1em)

#callout(
  "CAVOK Conditions",
  [
    CAVOK (Ceiling And Visibility OK) is used when:
    - Visibility 10 km or more
    - No cloud below 5000 ft or MSA (whichever higher)
    - No CB or TCU
    - No significant weather
  ],
  color: success,
  icon: "☀"
)

#pagebreak()

// ============================================================================
// SECTION 5: GENERATION PIPELINE
// ============================================================================

= Generation Pipeline

The generator creates realistic, diverse ATIS entries following a structured process.

== Flow Diagram

#align(center)[
  #canvas(length: 0.8cm, {
    import draw: *
    
    let step(x, y, num, label, color) = {
      rect((x, y), (x + 4, y + 1.5), fill: color.lighten(90%), stroke: 1.5pt + color, radius: 0.2)
      content((x + 2, y + 1), text(weight: "bold", fill: color)[#num])
      content((x + 2, y + 0.4), text(size: 8pt)[#label])
    }
    
    // Row 1
    step(0, 4, "1", "Select Airport", success)
    step(5, 4, "2", "Pick Difficulty", secondary)
    step(10, 4, "3", "Generate Info Letter", primary)
    
    line((4, 4.75), (5, 4.75), stroke: 1pt + neutral, mark: (end: ">"))
    line((9, 4.75), (10, 4.75), stroke: 1pt + neutral, mark: (end: ">"))
    
    // Row 2
    step(0, 1.5, "4", "Generate Weather", warning)
    step(5, 1.5, "5", "Select Runway", primary)
    step(10, 1.5, "6", "Build Full Text", success)
    
    line((4, 2.25), (5, 2.25), stroke: 1pt + neutral, mark: (end: ">"))
    line((9, 2.25), (10, 2.25), stroke: 1pt + neutral, mark: (end: ">"))
    
    // Connect rows
    line((14, 4.75), (14.5, 4.75), stroke: 1pt + neutral)
    line((14.5, 4.75), (14.5, 2.25), stroke: 1pt + neutral)
    line((14.5, 2.25), (14, 2.25), stroke: 1pt + neutral, mark: (end: ">"))
  })
]

#v(1em)

== Step Details

#grid(
  columns: 2,
  gutter: 1.5em,
  
  [
    === 1. Select Airport
    Random selection from 37 DACH airports. The airport provides:
    - ICAO code and name
    - Available runways
    - Transition altitude
    - Default frequency
    
    === 2. Pick Difficulty
    Based on target distribution:
    - super_easy: ~25%
    - easy: ~30%
    - medium: ~30%
    - hard: ~15%
    
    === 3. Generate Info Letter
    Sequential or random from NATO alphabet (Alpha–Zulu). Each letter identifies the ATIS version.
  ],
  
  [
    === 4. Generate Weather
    Based on difficulty settings:
    - Wind (direction, speed, gusts)
    - Visibility
    - Weather phenomena
    - Cloud layers
    - RVR (if low visibility)
    - Temperature, dewpoint, QNH
    
    === 5. Select Runway
    Choose appropriate runway based on:
    - Wind direction
    - ILS availability
    - Difficulty constraints
    
    === 6. Build Full Text
    Compose the spoken ATIS following ICAO phraseology standards.
  ],
)

#pagebreak()

== Example Outputs

#grid(
  columns: 2,
  gutter: 1em,
  
  block(
    width: 100%,
    stroke: 1.5pt + success,
    radius: 8pt,
    clip: true,
  )[
    #block(fill: success, width: 100%, inset: 8pt)[
      #text(fill: white, weight: "bold")[#difficulty-badge("super_easy") Example]
    ]
    #block(inset: 12pt, fill: white)[
      #set text(size: 9pt)
      #text(weight: "bold", fill: primary)[München Information Charlie]
      
      Recorded at 1420 Zulu
      
      Runway in use 26L
      ILS approach
      Transition level 70
      
      Wind calm
      CAVOK
      Temperature 20, dewpoint 12
      QNH 1020
      
      #text(style: "italic", fill: neutral)[
        Acknowledge receipt of information Charlie
      ]
    ]
  ],
  
  block(
    width: 100%,
    stroke: 1.5pt + danger,
    radius: 8pt,
    clip: true,
  )[
    #block(fill: danger, width: 100%, inset: 8pt)[
      #text(fill: white, weight: "bold")[#difficulty-badge("hard") Example]
    ]
    #block(inset: 12pt, fill: white)[
      #set text(size: 9pt)
      #text(weight: "bold", fill: primary)[Frankfurt Information Kilo]
      
      Recorded at 0835 Zulu
      
      Runway in use 25L for landing, 25C for departure
      ILS CAT III approach
      Transition level 60
      
      Wind 230 degrees 24 gusting 38 knots
      Visibility 400 meters, RVR runway 25L 550 meters
      Moderate rain, mist
      Broken 300 feet, overcast 800 feet
      Temperature 4, dewpoint 3
      QNH 998
      
      Low level wind shear reported on final.
      Braking action medium to poor.
      
      #text(style: "italic", fill: neutral)[
        Acknowledge receipt of information Kilo
      ]
    ]
  ],
)

#pagebreak()

// ============================================================================
// SECTION 6: API PATTERNS
// ============================================================================

= API Patterns

== Fetching ATIS Entries

Get entries with airport data:

```
GET /items/atis_entries?fields=
  id,
  information_letter,
  difficulty,
  full_text,
  wind_direction,
  wind_speed,
  visibility,
  qnh,
  airport.icao,
  airport.name
```

== Filter by Difficulty

```
GET /items/atis_entries
  ?filter[difficulty][_eq]=medium
  &limit=10
```

== Filter by Airport

```
GET /items/atis_entries
  ?filter[airport][icao][_eq]=EDDF
  &limit=5
```

== Random Selection for Practice

```
GET /items/atis_entries
  ?filter[difficulty][_eq]=easy
  &sort=rand()
  &limit=1
```

== Get Difficult Weather Conditions

```
GET /items/atis_entries
  ?filter[visibility][_lt]=1500
  &filter[difficulty][_eq]=hard
```

#v(2em)

#align(center)[
  #block(
    width: 70%,
    fill: bg-light,
    stroke: 1pt + border-light,
    radius: 8pt,
    inset: 1.5em,
  )[
    #text(size: 11pt, fill: neutral)[
      *Ready to practice?* The ATIS entries are designed to be \
      read aloud, matching real-world broadcast cadence.
    ]
    
    #v(0.5em)
    
    #text(size: 9pt, fill: neutral.lighten(30%))[
      Aevoli Pilot Training Platform · ATIS Schema v1.0
    ]
  ]
]
