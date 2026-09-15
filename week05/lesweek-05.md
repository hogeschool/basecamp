# Week 5 — Functions, Lists and Tuples

**Arch 2** · maandag 5 oktober t/m vrijdag 9 oktober 2026 · groep Ma/Wo

> Samengevoegd uit `Lesson plan - Week 5 - Day 1..4.docx` en `Instructions - Week 5 - Day 5.docx`.
> De originele bestanden staan in [`lesmateriaal/week05/`](../lesmateriaal/week05) — die map staat buiten git.

## Deadlines

| Wanneer | Wat | Waar |
|---|---|---|
| di 6 okt, eind van de dag | Exercises Step-01, Step-02 en Step-03 | zelf bijhouden |
| do 8 okt, eind van de dag | Problems en assignment af | zelf bijhouden |
| vr 9 okt 23:59 | Assignments inleveren | CodeGrade |

## Doelen van deze week

Uit het lesplan van de opleiding:

- Je leert hoe je een sequentiestructuur bouwt met basisdatatypen, en je leert meer mogelijkheden van functies.
- Je begint met testen.
- Je ontvangt feedback van je docenten, als basis voor een plan van aanpak.

### Programmeerdoelen per step

Uit [`week 5 voorbereiding.md`](./week%205%20voorbereiding.md). Na deze week kun je:

**Step-01: Tuples**

- :
- interpret and implement Python programs using tuples: creating, unpacking, modifying, combining two tuples, iterating over a tuple.

**Step-02: Lists**

- :
- interpret and implement Python programs using lists: defining, offset, slicing, adding new element, modifying an element.

**Step-03: Functions (more)**

- :
- interpret and implement Python programs with Python functions: positional arguments, keyword arguments, parameters default values, docstrings.

## Wat lever je in

| Code | Opdracht | Werkmap |
|---|---|---|
| `A2W5A1` | Packages data | [A2W5A1-packages-data/](./A2W5A1-packages-data) |
| `A2W5P1` | Automated arithmetics | [A2W5P1-automated-arithmetics/](./A2W5P1-automated-arithmetics) |
| `A2W5P2` | Taxi fares | [A2W5P2-taxi-fares/](./A2W5P2-taxi-fares) |
| `A2W5P3` | Triangle checker | [A2W5P3-triangle-checker/](./A2W5P3-triangle-checker) |
| `A2W5P4` | Integer checker | [A2W5P4-integer-checker/](./A2W5P4-integer-checker) |
| `A2W5P5` | Simple password generator | [A2W5P5-simple-password-generator/](./A2W5P5-simple-password-generator) |
| `A2W5P6` | Twelve days of christmas | [A2W5P6-twelve-days-of-christmas/](./A2W5P6-twelve-days-of-christmas) |

Problems en assignment af aan het eind van dag 4, inleveren in CodeGrade uiterlijk **vr 9 okt 23:59**. De A-opdracht telt mee voor het assessment; problems en oefeningen zijn ondersteunend bewijs.

## Extra oefenmateriaal

Optioneel. Niet in te leveren, wel goed materiaal om je vast te bijten als je klaar bent met de opdrachten van deze week.

- [Extra opdracht — Digital Library Management System](../extra-opdrachten/week05-digital-library.md)

## Waar deze week naartoe werkt — Arch 2

<details>
<summary>Leeruitkomsten van Arch 2 (bijlage C van de cursushandleiding)</summary>

**Professionele vaardigheden die aan bod komen**

- Leerstrategieën toepassen en evalueren
- Starten met feedback geven en ontvangen
- Plan van aanpak maken en ernaar handelen
- Onderzoeksvaardigheden uit Arch 1 herhalen en toepassen
- Problem solving toepassen
- Dossier opbouwen

**Na deze arch:**

- je kent verschillende methoden rond student succes en past die toe
- je weet wat belangrijk is bij het geven en ontvangen van feedback, en past dat toe
- je leert SMART-leerdoelen maken en daarnaar handelen
- je toont actieve betrokkenheid bij de eigen ontwikkeling, op basis van eerdere ervaringen en feedback
- je past geleerde onderzoeksvaardigheden toe
- je gaat verder met problem solving, met meer complexiteit
- je krijgt inzicht in het werkveld via een gastcollege

**Programmeerelementen in deze arch**

- functions: positional arguments, keyword arguments, default values, docstrings, anonymous functions
- lists: defining, offset, slicing, toevoegen, wijzigen, list comprehension
- tuples: creating, unpacking, modifying, combineren, itereren
- dictionaries: creating, items toevoegen en wijzigen, values/keys ophalen, deleting, pop, clear, itereren
- sets: creating, toevoegen en verwijderen, membership, itereren, intersection/union/difference/subset
- `copy()`, `deepcopy()`, nested structures

**Aan het eind van deze arch kun je:**

- het gedrag van een Python-programma lezen, begrijpen en analyseren met de elementen uit Arch 2
- oplossingen implementeren met functions, lists, tuples, sets en dictionaries
- debuggen en de basis van testen toepassen (input/output- en acceptatietesten)

</details>

## Dag 1 — maandag 5 oktober (on-site)

**Op het programma**

- Demo’s van de challenge week
- Vervolg feedbacksessies
- Activiteit Stadslab (BC11A, B, F)
- Supporting topic: Debugging & Testing (BC11C, D, G, H)
- Werken aan exercises met je leerteam

**Activiteiten**

- Stand-up.
- **Demo-time!** Elk team (of een paar individuen) laat in maximaal 10 minuten zien wat ze tijdens de challenge week hebben gemaakt: waar ben je trots op?
- Werken aan exercises Step-01 en Step-02 van week 5.
- Vervolg feedbacksessies.
- **Klassen BC11A, B, F — activiteit in het Stadslab.** BC11A 11.00–12.30, BC11B 14.30–16.00 op dag 1; BC11F 11.00–12.30 op dag 2. Lees de instructie vooraf en maak je keuze van tevoren.
- **Klassen BC11C, D, G, H — supporting topic: Testing & Debugging.** Waarom zijn testen en debuggen belangrijk? Debugtools en -strategieën lossen problemen sneller op en maken ontwikkelaars productiever. Testen en debuggen verbeteren zowel de softwarekwaliteit als de gebruikerservaring. Er hoort een opdracht bij; het resultaat gaat in je dossier.
- Stand-down.
- **Code analysis van deze week** — lees de code zelf: wat wordt de output? Bespreek en maak de opdrachten.

<details>
<summary>Notities voor de docent</summary>

- Op dag 2 is er een teamoverleg vanaf 13.00.

</details>

## Dag 2 — dinsdag 6 oktober (online)

**Op het programma**

- Werken aan exercises met je leerteam
- Lesmateriaal dag 3 voorbereiden
- Terugblik op de eerste online dag

**Activiteiten**

- Stand-up. Korte uitleg van de activiteiten; één lid per leerteam legt de aanpak uit.
- Werken aan exercises Step-02 en Step-03.
- Docentsessie voor vragen (zie het rooster).
- Stand-down.
- Optioneel: beginnen aan problems en assignments (af aan het eind van week 5).

## Dag 3 — woensdag 7 oktober (on-site)

**Op het programma**

- Werken aan exercises, problems en assignments in de klas
- Vervolg feedbacksessies
- Activiteit Stadslab (BC11C, D, G, H)
- Supporting topic: Debugging & Testing (BC11A, B, F)
- Instructies voor de online dag

**Activiteiten**

- Stand-up.
- In de klas werken: problems en, als je eraan toe bent, assignments in CodeGrade.
- Vervolg feedbacksessies.
- **Klassen BC11C, D, G, H — activiteit in het Stadslab.** BC11C 11.00–12.30 en BC11D 14.30–16.00 op dag 3; BC11G 11.00–12.30 en BC11H 14.30–16.00 op dag 4.
- **Klassen BC11A, B, F — supporting topic: Testing & Debugging** (zie dag 1).
- Stand-down.
- **Code analysis van deze week.**

<details>
<summary>Notities voor de docent</summary>

- Om 16.00 kort overleg met je sixpack.

</details>

## Dag 4 — donderdag 8 oktober (online)

**Op het programma**

- Doorwerken aan exercises, problems en assignments
- Peercoach
- Deadlines en onbegeleide dag nalopen

**Activiteiten**

- Stand-up.
- Doorgaan met problems en assignments in CodeGrade.
- Peercoaches bereikbaar via het Teams-kanaal “inloopruimte CMI-INF-Peercoaches” of op locatie.
- Stand-down.

## Dag 5 — vrijdag 9 oktober (onbegeleid)

Er is geen stand-up en geen les. Een onbegeleide dag gebruik je om bij te trekken (“Back on Track”), stof te herhalen of te verdiepen. Je kunt met je leerteam werken.

- Check je opdrachten in CodeGrade en Teams en maak alles van week 5 af.
- **Lever je assignments van week 5 in bij CodeGrade** — vandaag vóór 23:59.
- Neem het lesmateriaal van deze week nog eens door.
- Bereid het lesmateriaal van volgende week voor: wat staat er op de planning, wat heb je nodig?
- Altijd optioneel: Extra Steps, of alvast beginnen aan andere opdrachten.

## Lesmateriaal

Klik een bestand aan om het in Word, PowerPoint of je pdf-lezer te openen. Wat erin staat kun je ook doorzoeken via [`lesmateriaal/week05/INDEX.md`](../lesmateriaal/week05/INDEX.md) — daar staan per PowerPoint de slidetitels.

| Bestand | Soort | Submap |
|---|---|---|
| [Extra assignment week 5 - Digital Library Management System.docx](../lesmateriaal/week05/Lesson%20Material/Additional%20lesson%20material/Extra%20assignment%20week%205%20-%20Digital%20Library%20Management%20System.docx) | Word | Lesson Material/Additional lesson material |
| [Stadslab Rotterdam.docx](../lesmateriaal/week05/Lesson%20Material/Stadslab%20Rotterdam.docx) | Word | Lesson Material |
| [Supporting topic Arch 2 - Testing & Debugging.pptx](../lesmateriaal/week05/Lesson%20Material/Supporting%20topic%20Arch%202%20-%20Testing%20&%20Debugging.pptx) | PowerPoint | Lesson Material |
| [Supporting topic Testing & Debugging - Arch 2.docx](../lesmateriaal/week05/Lesson%20Material/Supporting%20topic%20Testing%20&%20Debugging%20-%20Arch%202.docx) | Word | Lesson Material |
| [debugging_address_book.py](../lesmateriaal/week05/Lesson%20Material/debugging_address_book.py) | Python | Lesson Material |
| [validation_test.py](../lesmateriaal/week05/Lesson%20Material/validation_test.py) | Python | Lesson Material |

---

Het programmeergedeelte van deze week staat in [`week 5 voorbereiding.md`](./week%205%20voorbereiding.md), je antwoorden in [`week 5 werkblad.md`](./week%205%20werkblad.md).
