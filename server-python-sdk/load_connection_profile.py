import os
from hfc.fabric import Client

current_dir = os.path.dirname(__file__)

network_file = os.path.join(
    current_dir, "..", "fabric-sdk-py", "test", "fixtures", "network.json"
)

cli = Client(net_profile=network_file)

print(cli.organizations)
print(cli.peers)
print(cli.orderers)
print(cli.CAs)
