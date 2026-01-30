import sys

def modify_features(filename, features_value):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        in_block = False
        for i, line in enumerate(lines):
            if '[features]' in line:
                in_block = True

            if in_block and line.strip().startswith(features_value[:10]):
                lines[i] = f"{features_value}\n"
                break

        with open(filename, 'w') as file:
            file.writelines(lines)

        print(f"Changes applied to {filename}")

    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <features_value>")
        sys.exit(1)

    filename = sys.argv[1]
    features_value = sys.argv[2]
    modify_features(filename, features_value)
