# Fantasy Book Generator

An implementation and expansion of the "Scroll and Codex" system from Autarch's [Axioms 14](https://www.drivethrurpg.com/product/406101/Axioms-Issue-14-Codex-and-Scroll) for [ACKS](https://www.drivethrurpg.com/product/99123/Adventurer-Conqueror-King-System) RPG system.

It produces an Excel file of fantasy books for use in libraries or treasure hoards.

I am a strictly amateur, self-taught programmer, and this was my first python code. Apologies for infelicities of style and algorithm.

## Download pre-made executable

If you just want to download and run the program:

1. download the zip file located in the "executable" folder on Git. Unzip it.

2. The first file after the folders will be a shortcut to acks_fpg.exe -- run it. The two Excel files created also have shortcuts directly beneath.

3. You should be able to ignore all other files unless you want to.

4. Note that there are two free-for-use fonts in the "font" folder that you may need to install on your system to see the flavor titles properly. This only needs to be done once.

## Features

* rapid generation of books--100 books can be generated in less than 30 seconds; 1000 can be done in under 5 minutes.
* Generate books by value (a fixed gp budget) or by number of volumes.
* A campaign-wide total number of books can be established. Thus, when new collections are generated, there is a chance (proportional to the number of books already discovered) to find another copy of the same book already generated.
* Random title generation;
* Random author name generation;
* Random translator (if application) name generation;
* Random subject generation;
* Random generation of "flavor title"--books in other languages are given "untranslated" titles as well. These use lorem ipsum text generators to create pseudo-Latin, Greek, Akkadian, Elvish, or Dwarvish titles;
* Generation tables in SQLite database;
* GUI interface via PySimpleGUI;
* Creation of Excel spreadsheets for ease of use;
* automatic archive of master list Excel files of generated books;
* quick access to campaign-wide stats on books (number of books created, number of unique volumes, total value of all books).
* each book automatically given a [UUID (universally unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier).

## Settings

From within the software, users can easily edit:
* languages not to be translated into (dead languages in the campaign can be translated, but newer works will not be translated into those dead languages)
* dice formula for additional years to be added to translation volume age
* chance of producing a translation
* chance of female authorship (default 50:50 for male:female) depending on historical milieu being simulated
* chance of a book being discovered that is incomplete
* chance that an author/translator will have a title (e.g., Doctor, Master, Magus, etc.)
* chance that an author/translator will have an epithet (e.g., the Fair, the Great, XIV, etc.)
* minimum age of book(s) generated
* maximum age of book(s) generated
* total number of books in campaign

## Other user-modifiable features

* Editing SQLite files allows additions or changes to:
    * templates for book title generation
    * first and last names
    * language groups for name generation
    * titles and epithets
    * tables which generate the library

    ([Consider SQLiteStudio](https://sqlitestudio.pl/) for easy GUI editing of these files.)

* Editing .txt files allows addition or change to lorem ipsum elements for foreign languages.

* Editing .yaml files for settings allows other parameters to be customized.

## Built in part with these libraries:
* [d20](https://pypi.org/project/d20/)
* [lorem text](https://github.com/TheAbhijeet/lorem_text)
* [openpyxl](https://pypi.org/project/openpyxl/)
* [pandas](https://pypi.org/project/pandas/)
* [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
* [uuid](https://docs.python.org/3/library/uuid.html)
* [yaml](https://pypi.org/project/PyYAML/)

## Icons:
* Settings Done by icon 54 from <a href="https://thenounproject.com/browse/icons/term/settings-done/" target="_blank" title="Settings Done Icons">Noun Project</a>
* Dismiss Setting by icon 54 from <a href="https://thenounproject.com/browse/icons/term/dismiss-setting/" target="_blank" title="Dismiss Setting Icons">Noun Project</a>
* Reset Settings by icon 54 from <a href="https://thenounproject.com/browse/icons/term/reset-settings/" target="_blank" title="Reset Settings Icons">Noun Project</a>
* Cog by icon 54 from <a href="https://thenounproject.com/browse/icons/term/cog/" target="_blank" title="cog Icons">Noun Project</a>
* Lost file by Viktor Vorobyev from <a href="https://thenounproject.com/browse/icons/term/lost-file/" target="_blank" title="Lost file Icons">Noun Project</a>
* Archive by Alain W. from <a href="https://thenounproject.com/browse/icons/term/archive/" target="_blank" title="archive Icons">Noun Project</a>
* Retry by Alice Design from <a href="https://thenounproject.com/browse/icons/term/retry/" target="_blank" title="retry Icons">Noun Project</a>
* Quit by VINZENCE STUDIO from <a href="https://thenounproject.com/browse/icons/term/quit/" target="_blank" title="quit Icons">Noun Project</a>
* Empty by Gregor Cresnar from <a href="https://thenounproject.com/browse/icons/term/empty/" target="_blank" title="Empty Icons">Noun Project</a>
* Coins by kliwir art from <a href="https://thenounproject.com/browse/icons/term/coins/" target="_blank" title="Coins Icons">Noun Project</a>
## License:

* [GNU GPL v3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Version 1.0.0
* initial public version

## Version 1.0.2
* Bug fix on age of book.

## Version 1.0.3
* Prevent endless loop if budget is too low despite repeated attempts to generate book, with overshoot enabled
* Check before run to be sure number of books asked is not zero.

## Version 1.0.4
* add a few more icons
* included pre-made executable

## Version 1.0.5
* tweak .gitignore file

## Version 1.1.0
* got rid of unneeded folders
* typos in README.md file