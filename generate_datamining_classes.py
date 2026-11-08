import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "discord-datamining" / "data" / "client" / "channels" / "stable" / "web" / "stylesheets" / "classes.json"
OUTPUT = ROOT / "datamining_classes.scss"


def main() -> None:
    classes = json.loads(SOURCE.read_text(encoding="utf-8"))
    lines = ["// Generated from discord-datamining classes.json.", ""]

    for shorthand, actual_class in classes.items():
        lines.extend(
            [
                f"${shorthand}: \".{actual_class}\";",
                "",
            ]
        )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
