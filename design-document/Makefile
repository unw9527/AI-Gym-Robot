FILES="main.tex"

.PHONY: all clean
all:
	pdflatex -shell-escape main.tex
	biber main
	pdflatex -shell-escape main.tex
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.bcf *.run.xml *.toc *.lof *.lot *.idx *.ind *.ilg *.glo *.gls *.acn *.acr *.alg *.glg *.glsdefs *.ist *.xdy *.pdf