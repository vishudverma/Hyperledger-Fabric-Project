import os
from hfc.fabric import Client

# file = os.path.abspath("../test/fixtures/network.json")

cli = Client(net_profile="/test/fixtures/network.json")

print(cli.organizations)
print(cli.peers)
print(cli.orderers)
print(cli.CAs)
