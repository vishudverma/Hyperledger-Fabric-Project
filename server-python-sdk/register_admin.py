import os
from hfc.fabric import Client
from hfc.fabric_ca.caservice import ca_service

# cli = Client(
#     net_profile=os.path.abspath(
#         "fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/connection-org1.yaml"
#     )
# )
#
relative_path = os.path.relpath(
    "./fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/connection-org1.yaml"
)
print(relative_path)
# ca_name = "ca.org1.example.com"
# cas = cli.CAs
#
# if cas:
#     cas = ca_service(target="http://localhost:17054", ca_certs_path="")
#     print(cas)
#
# admin_enrollment = org1_ca.enroll("admin", "admipw")
#
#
# def save_to_wallet(identity, name):
#     path = f"./wallet/{name}"
#     os.makedirs(path, exist_ok=True)
#     with open(f"{path}/certificate", "wb") as f:
#         f.write(identity["enrollmentCert"])
#     with open(f"{path}/private_key", "wb") as f:
#         f.write(identity["item"].private_key_export())
#
#
# save_to_wallet(admin_enrollment, "admin")
#
# user_id = "appUser1"
# user_secret = org1_ca.register(admin_enrollment, user_id)
#
# user_enrollment = org1_ca.enroll(user_id, user_secret)
# save_to_wallet(user_enrollment, user_id)
#
# print(f"Successfully registered and enrolled {user_id} and stored in wallet.")
