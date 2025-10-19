# war

Implementation of the casino variant of the card game "War" in Python.
See https://en.wikipedia.org/wiki/Casino_War.

## Overview

This project is a Python implementation of casino version of the card game "War" without betting.
It simulates a game where each player draws gets dealt a card from a shuffled deck, and the player with the highest card wins the round.
In case of a draw, three cards are burned (discarded) and another round is played to decide the draw.
The game continues until one there are no more cards left.
The player with the most won rounds wins the game.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/b3h3m0th/war.git
```

2. Activate the virtual environment

```bash
make activate
```

3. Install the requirements

```bash
make install
```

## Execution

```bash
make war
```

---

## Testing

```bash
make coverage
```
