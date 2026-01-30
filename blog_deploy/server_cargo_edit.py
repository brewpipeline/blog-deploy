import sys

def modify_dependencies(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        in_section = False
        for i, line in enumerate(lines):
            stripped = line.strip()

            if '[dependencies.blog-ui]' in stripped:
                in_section = True
                continue

            if in_section and stripped.startswith('['):
                break

            if in_section:
                if stripped.startswith('git = ') or stripped.startswith('tag = '):
                    lines[i] = '#' + lines[i]
                elif stripped.startswith('#path'):
                    lines[i] = lines[i].replace('#', '', 1)

        with open(filename, 'w') as file:
            file.writelines(lines)

        print(f"Changes applied to {filename}")

    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    modify_dependencies(filename)
