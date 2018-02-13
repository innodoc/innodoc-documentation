s/\\MSection{\([^}]*\)}/\\section{\1}/g;
s/\\MSubsection{\([^}]*\)}/\\subsection{\1}/g;
s/\\MSubsubsection{\([^}]*\)}/\\subsubsection{\1}/g;
s/\\MSubsubsubsectionx{\([^}]*\)}/\\paragraph{\1}/g;

s/\\begin{MSectionStart}//g;
s/\\end{MSectionStart}//g;

s/\\begin{MXContent}{\([^}]*\)}{\([^}]*\)}{\([^}]*\)}/\\subsubsection[\2]{\1}/g;
s/\\end{MXContent}//g;

s/\\MLabel{\([^}]*\)}/\\label{\1}/g;

s/\$\\backslash\$/\{\\textbackslash\}/g;

# just strip these
s/\\MPragma{MathSkip}//g;
s/\\MDeclareSiteUXID{[^}]*}//g;

s/\\MSsectionlabelprefix/Abschnitt/g;

# Separation von Aufzaehlung und Bedingung in Menge
s/\\MCondSetSep/{\\,}:{\\,}/g;

# Horizontaler Leerraum zwischen herausgestellter Formel und Interpunktion
s/\\MBlank/{\\ }/g;

# index
s/\\MEntry{\([^}]*\)}{\([^}]*\)}/\\textbf{\1}\\index{\2}/g;
s/\\MIndex{\([^}]*\)}/\\index{\1}/g;

# refs
s/\\MCRef{\([^}]*\)}/\\vref{\1}/g;
s/\\MRef{\([^}]*\)}/\\vref{\1}/g;
s/\\MERef{\([^}]*\)}/\\eqref{\1}/g;
s/\\MNRef{\([^}]*\)}/\\ref{\1}/g;
# \MSRef{LABEL_BASE_SITE_TWO}{Link}
s/\\MSRef{\([^}]*\)}{\([^}]\+\)}/\\hyperref[\1]{\2}/g;
# \MSRef{foo1}{}
s/\\MSRef{\([^}]*\)}{}/\\ref{\1}/g;
# \MSRef{foo1}
s/\\MSRef{\([^}]*\)}/\\ref{\1}/g;

# href
s/\\MExtLink{\([^}]*\)}{\([^}]*\)}/\\href{\1}{\2}/g;

# \verb
# \verb%\MSection{ABSCHNITTSTITEL}%
s/\\verb\%\([^%]*\)\%/\\verb\$\1\$/g;

# pandoc chokes on underscore, don't know why
s/EX_MLDROPDOWN_1/EXMLDROPDOWN1/g;
s/MA_SETS/MASETS/g;

# TODO
# - handle ifttm??
