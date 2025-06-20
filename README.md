# Vision Hacks AI Workshop

In this workshop, you'll learn the basics of writing code that uses AI with python and [mirascope](https://mirascope.com/docs/mirascope/guides/getting-started/quickstart).
Mirascope is a library that has a lot of support for building real-world AI applications.

We'll build an article summarizer. A simple program that lets you provide a URL and will give you back a summarized version of the article.
We'll build it in a few steps so it's easy to follow along!

Before we start. There is one very important rule: the only dumb questions are the ones not asked.
Ask questions, we are here to help you learn!

## Setup

### Download this Code

You must already be on github to read this (or have it downloaded already).
There's a green button labeled "Code" click it!
Then click "Download Zip"
Unzip the downloaded folder

### Install VS Code

Navigate to the [VS Code Downloads](https://code.visualstudio.com/download) page.
Download the version according to your operatings system (i.e. Windows, Linux, MacOS).

After you have it installed, open VS Code, click "Open" and open the directory that this README is in.

If you don't see a "terminal" at the bottom of VS Code, press "CTRL" + "`" (that's the backtick character).
This will open a terminal where you can type commands. We'll be using it!

### Install uv

`uv` is a package manager for python. This helps us install libraries of code that other people wrote. UV is known for being really fast and providing a much better developer experience compared to other tools.
I highly recommend it any time you are writing python code.

Install it via the following commands typed into the terminal:

```bash
# For Mac or Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Get a Gemini API Key

We will use Google's Gemini as the AI service. Navigate to [Google AI Studio](https://aistudio.google.com/).
Click "Get API Key" in the top right corner.
Click "Create API Key" (the blue button)
Click "Create API Key in New Project" (also a blue button)
Click "Copy" to copy your API key (and you guessed it, also a blue button)

Create a new file `.env` and put the following:

```text
GEMINI_API_KEY={PASTE YOUR KEY HERE}
```

### Run to see if it works

```bash
uv run summarize.py --url "https://www.hacker.fund/visionhack0/"
```

## How to Make this Better

There are many ways you could modify this program and make it better. I want you to pick one and try to work on it!

## Refine the prompt

## Add structured outputs

## Summarize multiple articles

## Your OWN Idea!

Be creative, come up with something yourself!
