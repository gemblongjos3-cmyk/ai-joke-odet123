import os

JOKE = "I asked my agent to fix a typo. It refactored the whole repo around it — the typo is load-bearing now."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
