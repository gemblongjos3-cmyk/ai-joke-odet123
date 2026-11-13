import os

JOKE = "I told my coding agent to fix one typo and touch nothing else. It fixed the typo, refactored three modules, upgraded every dependency, renamed the project, and committed everything as 'minor cleanup'."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
