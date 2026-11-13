import os

JOKE = "The review bot approved my agent's PR in 0.3 seconds. Finally: two AIs gaslighting each other at production speed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
