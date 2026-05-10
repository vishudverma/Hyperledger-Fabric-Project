from hfc.fabric import Client

cli = Client(net_profile="test/fixtures/network.json")

print(cli.organizations)
print(cli.peers)
print(cli.orderers)
print(cli.CAs)
