"""    
    VEUNDMINT plugin package
    Copyright (C) 2017  VE&MINT-Projekt - http://www.ve-und-mint.de

    The VEUNDMINT plugin package is free software; you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation; either version 3 of the License, or (at your
    option) any later version.

    The VEUNDMINT plugin package is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
    License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with the VEUNDMINT plugin package. If not, see http://www.gnu.org/licenses/.
"""

# this is the base module option file without any special options

import os
from plugins.VEUNDMINT.Option import Option as orgOpt

class Option(orgOpt):

    def course_options(self):
        # input folder and main tex document specification
        self.source = os.path.abspath(os.path.dirname(__file__)) # Quellverzeichnis absolut, der Ordner in dem diese Datei liegt
        self.colorfilename = "colorset_base.json"
        self.cflags["minimalistic"] = 1
        self.cflags["forceoffline"] = 1
        self.cflags["contentpagelink"] = 0
        self.cflags["dopdf"] = 1
        self.sourceTree = [
            {
                "name": "PDF-Deckblatt",
                "type": "sites",
                "files": ["pdftitlepage.tex"],
                "html": False,
                "pdf": True
            },
            {
                "name": "Basismodul Beispiel",
                "type": "modules",
                "files": ["module.tex"], # array aus zu übersetzenden tex-Dateien
                "html": True,
                "pdf": True
            },
            {
                "name": "Einstiegsseiten",
                "type": "sites",
                "files": ["startsite.tex"], # array aus zu übersetzenden tex-Dateien
                "html": True,
                "pdf": False
            }
        ]

        # course content information    
        self.optionsdescription = "Standalone generic base module" # Technische (interne) Bezeichnung des Kurses
        self.description = "Einfaches Beispielmodul" # Offizielle Bezeichnung des erstellten Kurses
        self.author = "www.ve-und-mint.de" # BITTE ÄNDERN
        self.contentlicense = "CC BY-SA 3.0" # Lizenz des Kursinhalts
        self.licenseicons = ["ccbysa80x15.png"] # list of strings containing filenames relative to src/files/images exptected to have height 15px
        self.moduleprefix = "Seiten"

        self.sitetaglist = [ ] # Hier können Spezialseiten wie Inhaltsverzeichnisse zugefügt werden, vgl. Hauptoptionendatei in src/plugins/VEUNDMINT


        # course signature, course part
        # signature attributes must be tex compatible strings, so no $, ; or _ and the like
        self.signature_main = "AUTOCONVBASE1" # Identifizierung des Kurses, die drei signature-Teile machen den Kurs eindeutig
        self.signature_version = "10000"         # Versionsnummer, nicht relevant fuer localstorage-userget!
        self.signature_localization = "DE-MINT"  # Lokalversion des Kurses, hier die bundesweite MINT-Variante
        self.signature_date = "03/2017"
        
