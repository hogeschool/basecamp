# Supporting topic — Testing & Debugging (Arch 2)

> Omgezet uit `Supporting topic Testing & Debugging - Arch 2.docx`.
> Het origineel staat in [`lesmateriaal/week05/Lesson Material`](../../lesmateriaal/week05/Lesson%20Material).
> Dit is het lege format van de opleiding — invullen doe je zelf.

---
2.2 Supporting topic week 5 – Debugging and Testing

[scroll down for English]

Testen

Laadt het bestand validation_test.py in. Je gaat nu testen uitvoeren waarmee je bepaalt of het programma de input van de gebruiker op de juiste wijze valideert. De input moet gevalideerd worden op basis van de requirements (eisen) die zijn opgesteld voor de applicatie. Je test het programma door inputtesten uit te voeren met verschillende data / testgevallen.

De requirements voor dit programma zijn:

Een naam mag alleen uit letters bestaan en bestaat uit minimaal 1 en maximaal 10 karakters.

Een leeftijd moet minimaal 0 en maximaal 120 zijn.

Een postcode moet bestaan uit 4 cijfers en twee letters, zonder spatie ertussen

Bij incorrecte invoer moet de gebruiker een foutmelding krijgen en moet de vereiste input opnieuw gevraagd worden.

Bedenk nu eerst welke data je wilt gaan gebruiken om de testen uit te voeren en zet deze in onderstaande tabel. Verleng de tabel indien nodig.

| requirement | testdata |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

Test het programma validation_test.py en noteer je bevindingen in onderstaande tabel. Verleng de tabel indien nodig.

Beschrijf welke bevindingen je hebt gedaan en met welke data je getest hebt (testgevallen):

| Bevinding | Gebruikte testdata |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |

Debugging

Laad het bestand debugging_address_book.py in, in de door jouw gebruikte code editor.

Analyseer de code en bepaal waar en hoe je begint met debuggen.

Vul voor iedere gevonden bug onderstaande tabel in. We geven eerst een voorbeeld.

## VOORBEELD

| Bevinding #Voorbeeld1 |  |
|---|---|
| Wat voor probleem veroorzaakt de bug? | Ingevuld contactformulier komt niet aan bij de web administrator |
| Waar in de code heb je de bug gevonden (regelnummer)? | In contact.php regel 55 staat het emailadres van de webadministrator. Er is .com in het adres gebruikt in plaats van .nl |
| Wat heb je gedaan om de bug te vinden? | Ik heb eerst gekeken welke source file werd uitgevoerd, daarna ben ik met de debugger door de send functie heen gegaan en viel het me op dat de email niet klopte. |
| Hoe heb je bug opgelost? | Ik heb het foute emailadres vervangen door het juiste. |

Vul nu zelf de tabellen in voor iedere gevonden bug.

| Bevinding #1 |  |
|---|---|
| Wat voor probleem veroorzaakt de bug? |  |
| Waar in de code heb je de bug gevonden (regelnummer)? |  |
| Wat heb je gedaan om de bug te vinden? |  |
| Hoe heb je bug opgelost? |  |

| Bevinding #2 |  |
|---|---|
| Wat voor probleem veroorzaakt de bug |  |
| Waar in de code heb je de bug gevonden (regelnummer)? |  |
| Wat heb je gedaan om de bug te vinden? |  |
| Hoe heb je bug opgelost? |  |

| Bevinding #3 |  |
|---|---|
| Wat voor probleem veroorzaakt de bug? |  |
| Waar in de code heb je de bug gevonden (regelnummer)? |  |
| Wat heb je gedaan om de bug te vinden? |  |
| Hoe heb je de bug opgelost? |  |

Verbeter de code op basis van jouw bevindingen. Voeg de verbeterde code toe als bijlage aan je dossier (zie hoofdstuk 3.1 in jouw dossier).

Beschrijf hier welke tips en bronnen je andere studenten kan geven over het leren debuggen.

…

…

…

2.2 Supporting topic week 5 – Debugging and Testing

Testing

Load the file validation_test.py. You will now perform tests to determine whether the programme validates the user's input correctly. The input must be validated based on the requirements set for the application. You test the programme by performing input tests with different data/test cases.

The requirements fort his program are:

A name may only consist of letters and must contain a minimum of 1 and a maximum of 10 characters.

An age must be minimum 0 and maximum 120.

A postcode must consist of 4 digits and two letters, without spaces in between.

In the event of incorrect input, the user must receive an error message and be asked to re-enter the required information.

First, consider which data you want to use to perform the tests and enter it in the table below. Extend the table if necessary.

| requirement | testdata |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

Test the program validation_test.py and record your findings in the table below. Extend the table if necessary.

Describe your findings and the data you used for testing (test cases):

| Finding | Used testdata |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |

Debugging

Load the file debugging_address_book.py, into the code editor you use.

Analyse the code and determine where and how to start debugging.

Fill in the table below for each bug found. We will first give an example.

## Example

| Finding # | Example1 |
|---|---|
| What kind of problem does the bug cause? | Completed contact form does not reach the web administrator |
| Where in the code did you find the bug (line number)? | In contact.php line 55, the email address of the web administrator is listed. The address uses .com instead of .nl. |
| What did you do to find the bug? | First, I checked which source file was being executed, then I went through the send function with the debugger and noticed that the email was incorrect. |
| How did you resolve the bug? | I have replaced the incorrect email address with the correct one. |

Now fill in the tables yourself for each bug found.

| Finding #1 |  |
|---|---|
| What kind of problem does the bug cause? |  |
| Where in the code did you find the bug (line number)? |  |
| What did you do to find the bug? |  |
| How did you resolve the bug? |  |

| Finding #2 |  |
|---|---|
| What kind of problem does the bug cause? |  |
| Where in the code did you find the bug (line number)? |  |
| What did you do to find the bug? |  |
| How did you resolve the bug? |  |

| Finding #3 |  |
|---|---|
| What kind of problem does the bug cause? |  |
| Where in the code did you find the bug (line number)? |  |
| What did you do to find the bug? |  |
| How did you resolve the bug? |  |

Improve the code based on your findings. Add the improved code as an attachment to your file (see section 3.1 in your file).

Describe here what tips and resources you can give other students about learning to debug.

…

…

…
