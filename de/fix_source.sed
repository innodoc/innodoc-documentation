################################################################################
# These patterns can be used to fix common errors in module.tex.
################################################################################

# pandoc chokes on % here. the form with $ works.
# \verb%\MBar{FOO}% -> \verb$\MBar{FOO}$
s/\\verb\%\([^%]*\)\%/\\verb\$\1\$/g;

# pandoc chokes on underscore in some cases (bug in pandoc?)
s/EX_MLDROPDOWN_1/EXMLDROPDOWN1/g;
s/MA_SETS/MASETS/g;

# missing protocol
s/\\MExtLink{www.mint-kolleg.de}/\\MExtLink{http:\/\/www.mint-kolleg.de\/}/g;

# ugly hack to create a backslash in a math env. no need to do this.
s/\$\\backslash\$/\{\\textbackslash\}/g;

# fix old LaTeX style umlaute, pandoc doesn't seem to support this
s/"o/ö/g;
s/"a/ä/g;
s/"u/ü/g;
s/"O/Ö/g;
s/"A/Ä/g;
s/"U/Ü/g;
