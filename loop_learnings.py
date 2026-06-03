domains = ["google.com", "github.com" , "meta.com"]

print("----Domains Subfinder----")

for site in domains:

    cmd = "Subfinder -d " + site

    print(cmd)