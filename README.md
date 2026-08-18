# Resume

Edit `_data/resume.yml` to maintain the website and generated PDF from one source.

Run the website locally with:

```sh
bundle install
bundle exec jekyll serve --baseurl=""
```

Generate the LaTeX source and PDF with:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/generate_resume.py
latexmk -pdf -interaction=nonstopmode -halt-on-error resume.tex
```

GitHub Pages publishes this project at `https://drsatrn.github.io/latex-master/`. The workflow derives the deployed base path from GitHub Pages, so moving to a custom domain does not require application code changes.
