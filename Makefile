PDFLATEX = pdflatex -interaction=batchmode -synctex=1
SH 		 = /bin/bash
ASCRIPT  = /usr/bin/osascript
MV = mv

SOURCE   = thesis.tex
BASE     = "$(basename $(SOURCE))"

default : pdf view 

.PHONY: pdf graphics
pdf: $(SOURCE)
	$(PDFLATEX) $(BASE) && bibtex $(BASE) && $(PDFLATEX) $(BASE) && $(PDFLATEX) $(BASE)

.PHONY: view
view: 
	$(SH) skim-view.sh $(BASE)

.PHONY: clean
clean :
	#$(RM) -f -- *.aux *.bak *.bbl *.blg *.log *.out *.toc *.tdo _region.*
	$(MV) thesis.aux output_file/
