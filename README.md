# Python_Mini_Projects
Range of python coding practice by solving problems on Codewars and building a bingo game from inspiration.


# Requirements
Recommended IDE: PyCharm (although any text/code editor or IDE would work fine)
Python version: 3.8+ (although it can technically use Python 3.6+, but possibly unsafe)


# Instructions and Terminal Commands
git clone 'github link to repo'
python Codewars_Practice.py (although you need to write some code to see the effects of the functions, it's been tested by Codewars tests and all functions/classes have passed)
python Mini_Bingo_Game.py
(Sometimes 'python3' should be used in command instead of 'python')


# Notes
This repository is primarily for learning and practice, not production use.
Some solutions prioritise clarity and experimentation over optimal efficiency.
Code is continuously evolving as new Kata are solved.


# About & Features
---
The goal of this repo is to improve problem-solving skills, strengthen Python fundamentals, and practice writing clean, modular functions.

## 🚀 Features

### 🧩 Codewars Practice (`Codewars_Practice.py`)
A large collection of Python functions covering:

#### 🔹 8 kyu – Fundamentals
- String manipulation (e.g. alternating case, remove characters)
- Basic arithmetic logic
- Dictionary-based name generation
- Simple class design (`Hero`, `User`)

#### 🔹 7 kyu – Intermediate Logic
- Square numbers & digit manipulation
- Array transformations
- String parsing (camelCase, disemvoweling)
- Mathematical problems (summation, binary conversion)
- Data validation and filtering

#### 🔹 6 kyu – Advanced Problem Solving
- Pattern matching & encoding (`duplicate_encode`)
- Sorting and array reconstruction
- Queue simulation problems
- Binary parity checking
- Chess board validation to FEN conversion
- Custom data structures (e.g. `WordDictionary`, `Potion`, `Robot`)

---

### 🎮 Mini Bingo Game (`Mini_Bingo_Game.py`)

A terminal-based interactive bingo simulation where:

- Users define:
  - Card size
  - Number range
  - Number of draws
- A random bingo card is generated
- Numbers are drawn sequentially
- Matches are tracked in real-time
- Game ends when:
  - All numbers are matched (**BINGO!**) or
  - Draws finish

#### Example Gameplay:
```
Your Bingo Card: [3, 18, 7, 22]

Number drawn: 7
Match found!
Current score: 1/4
```
