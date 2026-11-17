# Python Programming Internship Projects

This repository contains Python projects developed as part of my Python Programming Internship at Datheon.

These projects focus on developing practical programming skills, problem-solving techniques, data structures, automation, and file handling using Python.

## Projects

### 1. Hangman Word Guessing Game

A Python-based console game where players try to guess a hidden word by entering letters before running out of attempts.

**Features:**
- Random word selection.
- Letter-by-letter guessing.
- Tracks correct and incorrect guesses.
- Prevents duplicate guesses.
- Displays Hangman stages.
- Win and lose conditions.

**Technologies:** Python, Random Module, Loops, Conditional Statements, Sets.

**Project Folder:** `Hangman/`

### 2. Investment Portfolio Tracker

A Python-based application that helps users track stock investments and monitor portfolio performance.

Users can enter stock ticker symbols, purchase prices, and share quantities. The application retrieves current stock prices using Yahoo Finance and calculates investment value, profit, and loss.

**Features:**
- Add stock ticker symbols.
- Enter purchase prices and share quantities.
- Fetch current stock prices using yfinance.
- Calculate total invested capital.
- Calculate current market value.
- Calculate individual stock profit/loss.
- Calculate overall portfolio performance.
- Automatically export portfolio summaries to CSV.
- Handle invalid inputs and price retrieval errors.

**Technologies:** Python, CSV Module, yfinance, File Handling, Dictionary Data Structure.

**Project Folder:** `Investment_Portfolio_Tracker/`

**Installation:**
```bash
pip install yfinance
```

**Execution:**
```bash
python portfolio.py
```

### 3. Rule-Based Customer Support Chatbot

A Python-based interactive chatbot that responds to customer queries using predefined FAQs, keyword matching, and regular expressions.

The chatbot loads questions and answers from a JSON dataset and provides relevant responses to user queries.

**Features:**
- Greeting detection.
- Business hours information.
- Internship project submission guidance.
- Certificate-related FAQs.
- Keyword-based intent identification.
- Regular expression-based text matching.
- Multiple-intent matching.
- Fallback responses for unrecognized queries.
- Exit commands such as `bye`, `exit`, and `quit`.
- Error handling and JSON file processing.

**Technologies:** Python, JSON, Regular Expressions (`re`), File Handling.

**Project Folder:** `Rule_Based_Chatbot/`

**Execution:**
```bash
python chatbot.py
```

## Technologies Used

- Python 3
- VS Code
- Git and GitHub
- CSV Module
- JSON
- Regular Expressions
- File Handling
- Python Data Structures

## Repository Structure

```text
Datheon_Python_Programming_Internship/
│
├── Hangman/
│   └── hangman.py
│
├── Investment_Portfolio_Tracker/
│   ├── portfolio.py
│   └── README.md
│
├── Rule_Based_Chatbot/
│   ├── chatbot.py
│   ├── faq.json
│   └── README.md
│
└── README.md
```

## Author

**Aksha Dev A**

B.Tech Computer Science and Engineering

GitHub: [akshadev005-hub](https://github.com/akshadev005-hub)
