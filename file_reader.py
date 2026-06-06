with open("targets.txt", "r") as file:
    domains = file.readlines()
    for site in domains:
        print("Loaded target from TXT file: " + site)