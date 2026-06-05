domains = ["google.com", "attacker.com" , "meta.com"]

for site in domains:
    print("Scanning for clean targets: " + site)

    if site == "attacker.com":
        print("Alert: " + site + " is a known malicious domain.")
    else:
        print(site + " is a clean target.")