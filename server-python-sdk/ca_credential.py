from hfc.fabric_ca.caservice import ca_service

casvc = ca_service(target="https://172.17.0.1:7054")
adminEnrollment = casvc.enroll("admin", "adminpw")
secret = adminEnrollment.register("user1")
user1Enrollment = casvc.enroll("user1", secret)
user1ReEnrollment = casvc.reenroll(user1Enrollment)
RevokedCerts, CRL = adminEnrollment.revoke("user1")
