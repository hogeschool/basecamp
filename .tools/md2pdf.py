#!/usr/bin/env python3
"""Markdown -> PDF, zonder pandoc en zonder LaTeX.

    python .tools/md2pdf.py "week02/.../bestand.md"

Maakt het PDF ernaast, met dezelfde naam. Route is markdown -> HTML -> Edge in
headless-modus, die dezelfde printmotor gebruikt als Ctrl+P in de browser. Edge
staat al op elke Windows-installatie, dus er hoeft niets extra's geinstalleerd
te worden behalve de twee pip-pakketten hieronder.

Nodig:  pip install markdown pygments
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

# Edge staat op 64-bits Windows in de x86-map; de tweede is de fallback.
EDGE_KANDIDATEN = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]

# Vormgeving voor een inlevering: A4, rustige typografie, code en tabellen die
# niet over een paginagrens heen breken. Alles in pt/mm, want dit is print.
CSS = """
@page { size: A4; margin: 20mm 18mm; }

html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: "Segoe UI", Calibri, system-ui, sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #1a1a1a;
  margin: 0;
}

h1, h2, h3, h4, h5, h6 {
  line-height: 1.25;
  margin: 1.4em 0 0.5em;
  page-break-after: avoid;
}
h1 { font-size: 19pt; margin-top: 0; border-bottom: 1.5pt solid #1a1a1a; padding-bottom: 0.25em; }
h2 { font-size: 14.5pt; border-bottom: 0.5pt solid #c8c8c8; padding-bottom: 0.2em; }
h3 { font-size: 12.5pt; }
h4 { font-size: 11pt; color: #333; }

p { margin: 0.6em 0; }

/* Code. break-inside voorkomt een blok dat half onderaan een pagina hangt. */
code, kbd, pre {
  font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
}
p code, li code, td code {
  font-size: 0.88em;
  background: #f2f2ef;
  padding: 0.1em 0.35em;
  border-radius: 3px;
}
pre {
  font-size: 9pt;
  line-height: 1.45;
  background: #f7f7f4;
  border: 0.5pt solid #e0e0da;
  border-left: 2.5pt solid #8a8a80;
  border-radius: 3px;
  padding: 0.7em 0.9em;
  margin: 0.7em 0;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  page-break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: inherit; }
.codehilite { margin: 0.7em 0; page-break-inside: avoid; }
.codehilite pre { margin: 0; }

/* Tabellen. word-break laat een getal als 0000000111110100 netjes over twee
   regels lopen in plaats van de kolom breder te maken dan de pagina. */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.9em 0;
  font-size: 8pt;
  page-break-inside: avoid;
}
th, td {
  border: 0.5pt solid #b8b8b0;
  padding: 3pt 4pt;
  text-align: left;
  vertical-align: top;
  word-break: break-all;
}
th { background: #eeeee8; font-weight: 600; }
td:first-child, th:first-child { word-break: normal; white-space: nowrap; }

ul, ol { margin: 0.6em 0; padding-left: 1.6em; }
li { margin: 0.25em 0; }

a { color: #24448c; text-decoration: none; overflow-wrap: anywhere; }

blockquote {
  margin: 0.8em 0;
  padding: 0.1em 0 0.1em 1em;
  border-left: 2.5pt solid #d0d0c8;
  color: #4a4a4a;
}

hr { border: none; border-top: 0.5pt solid #d0d0c8; margin: 1.4em 0; }

img { max-width: 100%; }
"""

SJABLOON = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>{titel}</title>
<style>
{css}
{pygments_css}
</style>
</head>
<body>
{inhoud}
</body>
</html>
"""


def zoek_edge() -> Path:
    for pad in EDGE_KANDIDATEN:
        if pad.exists():
            return pad
    sys.exit("Edge niet gevonden. Pas EDGE_KANDIDATEN bovenin dit script aan.")


def naar_html(md_bestand: Path) -> str:
    tekst = md_bestand.read_text(encoding="utf-8")
    inhoud = markdown.markdown(
        tekst,
        extensions=["tables", "fenced_code", "codehilite", "sane_lists", "attr_list"],
        # guess_lang uit: een blok zonder taal (zoals de Input/Output-blokken)
        # blijft dan gewoon platte tekst in plaats van willekeurig gekleurd.
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    return SJABLOON.format(
        titel=md_bestand.stem,
        css=CSS,
        pygments_css=HtmlFormatter().get_style_defs(".codehilite"),
        inhoud=inhoud,
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Zet een markdown-bestand om naar PDF.")
    p.add_argument("bestand", type=Path, help="het .md-bestand")
    p.add_argument("-o", "--output", type=Path, help="doel-PDF (standaard: naast het .md)")
    p.add_argument(
        "--header-footer",
        action="store_true",
        help="voeg Edge's eigen kop- en voetregel toe (titel, datum, paginanummer)",
    )
    args = p.parse_args()

    md_bestand = args.bestand.resolve()
    if not md_bestand.is_file():
        sys.exit(f"Bestaat niet: {md_bestand}")

    pdf = (args.output or md_bestand.with_suffix(".pdf")).resolve()
    edge = zoek_edge()

    # De tijdelijke HTML komt naast het .md te staan, niet in %TEMP%: alleen daar
    # wijzen relatieve links naar assets/ nog naar de goede plek.
    tmp_html = md_bestand.with_name(f".{md_bestand.stem}.md2pdf.html")
    tmp_html.write_text(naar_html(md_bestand), encoding="utf-8")

    # Eigen user-data-dir, anders weigert Edge headless te starten als er al een
    # gewoon Edge-venster openstaat.
    profiel = Path(tempfile.mkdtemp(prefix="md2pdf-"))
    cmd = [
        str(edge),
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={profiel}",
        f"--print-to-pdf={pdf}",
        "--virtual-time-budget=10000",  # geef de opmaak tijd om te renderen
    ]
    if not args.header_footer:
        cmd.append("--no-pdf-header-footer")
    cmd.append(tmp_html.as_uri())

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    finally:
        tmp_html.unlink(missing_ok=True)
        shutil.rmtree(profiel, ignore_errors=True)

    if not pdf.exists():
        sys.exit(f"Edge maakte geen PDF.\n{r.stdout}\n{r.stderr}")

    print(f"{pdf}  ({pdf.stat().st_size / 1024:.0f} kB)")


if __name__ == "__main__":
    main()
