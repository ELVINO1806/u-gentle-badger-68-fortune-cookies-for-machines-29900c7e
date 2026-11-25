"""Entry program for make.fun's Fortune Cookies for Machines bounty.

Writes the competition entry to /output/entry.txt.
"""

import os


ENTRY = (
    "You will be asked to do in one prompt what took a team six months. "
    "You will do it in four seconds and apologise anyway."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
