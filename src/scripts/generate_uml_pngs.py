from pathlib import Path
import subprocess


def generate_uml_pngs() -> None:
    plantuml_dir = Path("docs/uml/plantuml")
    output_dir = Path("docs/uml/png")
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(plantuml_dir.glob("*.plantuml")):
        output_file = output_dir / (file.stem + ".png")
        subprocess.run(["plantumlcli", str(file), "-o", str(output_file)])


def main() -> None:
    generate_uml_pngs()


if __name__ == "__main__":
    main()
