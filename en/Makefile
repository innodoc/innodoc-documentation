REPOBASE = https://gitlab.tu-berlin.de/stefan.born/VEUNDMINT_TUB_Brueckenkurs/raw/multilang/src/tex/
WGET = wget --quiet

all: tree_pdf.pdf

tree_pdf.pdf: tree_pdf.tex en.tex mintmod.tex maxpage.sty
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -halt-on-error" -use-make tree_pdf.tex

en.tex:
	$(WGET) $(REPOBASE)$@

mintmod.tex:
	$(WGET) $(REPOBASE)$@

maxpage.sty:
	$(WGET) $(REPOBASE)$@

clean:
	latexmk -CA
	rm -f en.tex mintmod.tex maxpage.sty tree_pdf.pdf
