
# SolarSystem

This is a console-based application that allows the user to ask questions in order to retrieve facts and information on the planets of the Solar System

- Displays facts about all planets or specific planets.
- Displays specific facts about Pluto.
- Allows for a tabular comparison of all facts for all planets, or a single fact for all planets.


## Chat Bot

The chat bot feature was implemented based on a guide from Indently [1]. I utilised the basic algorithms, but extended it to
produce modified responses that would allow me to perform custom actions. This required me to add so helper functions to 
parse the responses and format the outputs.

### How it works

The chat bot allows the user to enter questions such as:

- Tell me everything about the planets
- Tell me everything about Saturn
- What is the mass of Satrun?
- Compare all planets
- Compare the mass of all planets?

You can even greet the chatbot, and say goodbye to quit the application.

## Technical Details

### Version

The application was built using Python 3.15

### Modules

The required modules for the project can be loaded using the requirements document.

#### Windows

> python -m venv .venv
> 
> .\\.venv\\Scripts\\activate
> 
> python -m pip install -r requirements.txt

#### Linux or Mac

> python -m venv .venv
> 
> .\\.venv\\bin\\activate
> 
> python -m pip install -r requirements.txt


## Modules

### Tabulate

Tabular is a package that neatly presents data into tables [2]. It would have been possible to create my own table formatting class, but as the 
tabular display was not a key component of the assignment, I chose to use a pre-existing package.


## References

[1] Indently (2021) "How to create an accurate Chat Bot Response System in Python Tutorial (2021)". *https://www.youtube.com/watch?v=Ea9jgBjQxEs* Accessed on: 30/06/2025

[2] Python Software Foundation (2025) "tabulate 0.9.0" from PyPi.org. *https://pypi.org/project/tabulate/* Accessed on: 07/07/2025
