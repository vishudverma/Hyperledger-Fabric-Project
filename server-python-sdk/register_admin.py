import json
import os
from hfc.fabric_ca.caservice import CAService


def find_file(filename: str, search_path: str):
    for dirpath, _, filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None


def main():
    net_path = find_file("connection-org1.json", os.getcwd())
    if not net_path:
        print("There is no connection-org1.json file available.")
    with open(net_path) as file:
        ccp = json.load(file)

    ca_info = ccp["certificateAuthorities"]["ca.org1.example.com"]
    ca_url = ca_info["url"]
    ca_cert_path = os.path.relpath(
        "./fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/cacerts/localhost-7054-ca-org1.pem"
    )

    casvc = CAService(target=ca_url, ca_certs_path=ca_cert_path)
    admin = casvc.enroll("admin", "adminpw")
    # Until this point we create admin for org1
    print(admin)


if __name__ == "__main__":
    main()
