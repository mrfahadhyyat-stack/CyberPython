domains = ["google.com", "attacker.com" , "meta.com"]

for site in domains:

    if site == "attacker.com":
        print("Alert: " + site + " is a known malicious domain.")
    else:
        print(site + " is a clean target.")
        print("Scanning for clean targets: " + site)