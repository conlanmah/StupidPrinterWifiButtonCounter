import sys

def keypress_instructions(password: str):
    rotation = "~}|{zyxwvutsrqponmlkjihgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)('&%$#\"!"
    instructions = []

    for char in password:
        if char not in rotation:
            instructions.append(f"{char} not in rotation")
            continue

        down_index = rotation.index(char)
        up_index = len(rotation) - 1 - rotation[::-1].index(char)

        down_presses = 2 + down_index
        up_presses = 2 + (len(rotation) - 1 - up_index)

        if down_presses <= up_presses:
            instructions.append(f"{char}: down {down_presses}")
        else:
            instructions.append(f"{char}: up {up_presses}")

    return instructions

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    results = keypress_instructions(password)

    for line in results:
        print(line)

if __name__ == "__main__":
    main()
