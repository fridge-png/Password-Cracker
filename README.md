# Password Cracker
Password Cracker Code as a challenge in my Cybersecurity Master's. 

## Functionality

Assuming that a shadow file is available, the code checks for each user in the shadow file and cracks the password.
The passwords are hashed using different hashing algorithms such as md5, sha256, and sha512

The code uses a common password dictionary (separated into dic1,dic2,dic3,dic4 txt files for thread utilization). The passwords are hashed with the respective algorithm and tested against the passwords in the shadow files. If any passwords are found, they are printed to a new file. 