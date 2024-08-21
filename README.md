# AnkiAutomatorNotes
This program is a note automator in Anki.
### What is Anki?
Anki is a program which makes remembering things easy. Because it's a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

Anyone who needs to remember things in their daily life can benefit from Anki. Since it is content-agnostic and supports images, audio, videos and scientific markup (via LaTeX), the possibilities are endless.
For example:

- Learning a language
- Studying for medical and law exams
- Memorizing people's names and faces
- Brushing up on geography
- Mastering long poems
- Even practicing guitar chords!
### Why use this automator?
If you need to write a lot of sentences, this program can help you minimize the work of doing so.
### [Installation server Anki](https://foosoft.net/projects/anki-connect/)
Follow the instructions: https://foosoft.net/projects/anki-connect/
### How to use this program?
In the Data.py file, there is a variable 'texto_extraido' in which you insert the text with the following formatting:
```ruby
texto_extraido = """
Frase 1
  Frente:
  Hello World!
  Verso: 
  Olá Mundo!
Frase 2
  Frente:
  -------
  Verso:
  -------
"""
```
In Main.py, there is a variable 'deckName' in which you enter the name of the Deck:
```ruby
deckName = "Learn English"
```
