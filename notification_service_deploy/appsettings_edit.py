import json
import sys

def modify_appsettings(file_path, settings_dict):
    appsettings = json.load(open(file_path))

    for section, props in json.loads(settings_dict).items():
        if section in appsettings:
            apply_settings(appsettings[section], props)

    with open(file_path, 'w') as f:
        json.dump(appsettings, f, indent=2)


def apply_settings(section, props):
    for key, value in props.items():
        if key in section:
            section[key] = value

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filepath> <settings>")
        sys.exit(1)

    file_path = sys.argv[1]
    settings_dict = sys.argv[2]
    modify_appsettings(file_path, settings_dict)