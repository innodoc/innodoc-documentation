# Example file for course settings
# If you remove it or change it, probably some tests will fail. Have that in mind.

# Define a new setting in the base plugin
BASE_COURSE_SETTING = 'new value'

# Overwrite the course title
#description = 'Basis-Beispielmodul'

de = {
        "description": "Basis-Beispielmodul",
        "wikipedia": {
                "categories" : [
                        "Rhetorischer_Begriff","Testen_(Software)","Qualitätsmanagement (Softwaretechnik)"
                ],
                "blacklist" : [ "Basis" ]
        }
}

en = {
        "description": "Example module",
        "wikipedia": {
                "categories" : [
                        "Figures_of_speech","Software_testing","Software_quality"
                ],
                "blacklist" : [ "Base" ]
        }
}
