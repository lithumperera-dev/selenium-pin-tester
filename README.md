# Selenium PIN Tester

A simple Python project using **Selenium** to automate a local login page and test 4-digit PIN combinations.

## Features

* Automates a browser using Selenium
* Tests 4-digit PIN combinations
* Clears the input field between attempts
* Detects when the correct PIN is found
* Stops automatically when successful
* Uses a local HTML page for safe testing

## Technologies Used

* Python
* Selenium
* HTML
* JavaScript

## How It Works

The Python script loops through PIN combinations:

```text
0000
0001
0002
...
9999
```

Selenium enters each PIN into the local login page and checks whether the PIN is correct.

## Installation

Install Selenium:

```bash
pip install selenium
```

## Running the Project

Start the local web server:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/login.html
```

Run the Python program:

```bash
python3 main.py
```

## What I Learned

This project helped me practise:

* Python loops
* Selenium browser automation
* HTML forms
* Finding HTML elements using IDs
* Sending input using Selenium
* Automating repetitive browser actions

## Disclaimer

This project was created for **educational purposes and local testing only**.

Only use automated login testing on systems that you own or have permission to test.
