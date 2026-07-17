"""Build script: template.html + data/*.json -> docs/index.html

Run from the project root:

    python scripts/pipeline.py

What it does, and why it is this boring: it reads the small hand-edited
template, inlines the JSON data into it, and writes a single self-contained
page into docs/. That is the whole build. GitHub Pages serves docs/ directly,
so there is no server, no framework, and nothing to keep running.

The template keeps a fetch fallback, so it also works un-built during
development. This script only ever produces the shippable version.
"""

from datetime import date  # Python months are 1-indexed
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template.html"
DATA = ROOT / "data" / "metrics.json"
OUT_DIR = ROOT / "docs"
OUT = OUT_DIR / "index.html"

# The exact line in template.html that gets replaced. If you edit the template,
# keep this line byte-identical or the build will fail loudly (which is the point).
PLACEHOLDER = "const PRELOADED_DATA = {}; /*__DATA__*/"


def fail(msg: str) -> None:
    """Fail loudly. A build that half-works and writes a broken page is worse
    than one that stops and tells you why."""
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not TEMPLATE.exists():
        fail(f"{TEMPLATE} not found. Run this from the project root.")
    if not DATA.exists():
        fail(f"{DATA} not found.")

    try:
        data = json.loads(DATA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{DATA} is not valid JSON: {e}")

    # Stamp the build date from the system clock rather than trusting the JSON
    # to have been kept current by hand.
    data.setdefault("meta", {})["last_updated"] = date.today().isoformat()

    html = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in html:
        fail(
            "Placeholder line not found in template.html. It must contain, exactly:\n"
            f"  {PLACEHOLDER}"
        )

    # separators= keeps the payload compact; ensure_ascii=False keeps real
    # characters readable rather than escaping them into noise.
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    html = html.replace(PLACEHOLDER, f"const PRELOADED_DATA = {payload};")

    OUT_DIR.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")

    kb = len(html.encode("utf-8")) / 1024
    # Console output stays plain ASCII: some Windows terminals default to cp1252
    # and raise UnicodeEncodeError on anything fancier.
    print(f"Built {OUT.relative_to(ROOT)} ({kb:.1f}KB) - data stamped {data['meta']['last_updated']}")
    if kb > 500:
        print("Note: output is over 500KB. Never open it by hand; edit template.html instead.")


if __name__ == "__main__":
    main()
