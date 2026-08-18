from pathlib import Path
import argparse

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined


ROOT = Path(__file__).resolve().parents[1]


def tex(value):
    value = str(value or "").replace("’", "'").replace("–", "--")
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def tex_url(value):
    return str(value or "").replace("%", r"\%").replace("#", r"\#")


def visible(items):
    return [item for item in (items or []) if item.get("enabled", True)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=ROOT / "_data" / "resume.yml")
    parser.add_argument("--template", default="resume.tex.j2")
    parser.add_argument("--output", type=Path, default=ROOT / "resume.tex")
    args = parser.parse_args()

    with args.data.open(encoding="utf-8") as source:
        resume = yaml.safe_load(source)

    environment = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        comment_start_string="((#",
        comment_end_string="#))",
    )
    environment.filters["tex"] = tex
    environment.filters["tex_url"] = tex_url
    environment.filters["visible"] = visible
    rendered = environment.get_template(args.template).render(resume=resume)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
