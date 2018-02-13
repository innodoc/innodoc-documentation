REPOBASE = https://gitlab.tu-berlin.de/stefan.born/VEUNDMINT_TUB_Brueckenkurs/raw/multilang/src/tex/
WGET = wget --quiet

all: tree_pdf.pdf

de.tex:
	$(WGET) $(REPOBASE)$@

mintmod.tex:
	$(WGET) $(REPOBASE)$@

maxpage.sty:
	$(WGET) $(REPOBASE)$@

tree_pdf.pdf: tree_pdf.tex de.tex mintmod.tex maxpage.sty
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -halt-on-error" -use-make tree_pdf.tex

module.html: module_preprocessed.tex
	pandoc -f latex -t html5+empty_paragraphs -s --verbose --mathjax --toc --toc-depth=3 -o $@ module_preprocessed.tex

module_preprocessed.tex: replace_patterns.sed module.tex
	sed -f replace_patterns.sed module.tex > $@

clean:
	latexmk -CA
	rm -f de.tex mintmod.tex maxpage.sty tree_pdf.pdf module_preprocessed.tex module.html

.PHONY: all clean
