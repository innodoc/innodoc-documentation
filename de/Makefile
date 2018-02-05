REPOBASE = https://gitlab.tu-berlin.de/stefan.born/VEUNDMINT_TUB_Brueckenkurs/
WGET = wget --quiet

all: tree_pdf.pdf

tree_pdf.pdf: tree_pdf.tex mintmod.tex maxpage.sty
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -halt-on-error" -use-make tree_pdf.tex

mintmod.tex:
	$(WGET) $(REPOBASE)raw/multilang/src/tex/$@

maxpage.sty:
	$(WGET) $(REPOBASE)raw/multilang/src/tex/$@

clean:
	latexmk -CA
	rm -f mintmod.tex maxpage.sty tree_pdf.pdf
