# Store  word meanings in a python dictionary:
dictionary = {
  "Cybersecurity":"Protecting systems and data from attacks",
  "Firewall":"Security system that blocks threats",
  "Ransomware":"Malware that locks data for money",
  "Data Breach":"Unauthorized data access or leak"
}
for term, meaning in dictionary.items():
    print(term, ":", meaning)