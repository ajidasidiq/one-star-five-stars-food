#!/usr/bin/env python3
"""Write our one-star alien review of Earth to /output/entry.txt.

The entry is a single sentence, at most 200 characters, in the voice of
an alien tourist: a one-star review of planet Earth that still slips in
a real compliment about the food.
"""

import os

ENTRY = "One star: your species pays for water, worships glowing rectangles, and queues for bitter bean juice \u2014 but the dumplings were so good I nearly defected and opened a stall."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
