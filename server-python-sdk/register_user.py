import json
from hfc.fabric_ca.caservice import ca_service
from hfc.fabric import Client
import os


def find_file(filename, search_path):
    for dirpath, _, filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None


def main():
    net_path = find_file("connection-org1.json", os.getcwd())  # noqa: F841
    if not net_path:
        print("There is no connection-org1.json file available.")
    else:
        with open(net_path) as file:
            net_conf = json.load(file)


if __name__ == "__main__":
    main()
