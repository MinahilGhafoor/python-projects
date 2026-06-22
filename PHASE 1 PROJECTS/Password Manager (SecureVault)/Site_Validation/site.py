import requests

def isValidSite(site):
    if not site.startswith("http"):
        site = "https://" + site

    try:
        print()
        response = requests.get(site, timeout=15)
        return response.status_code < 400

    except:
        return False

def getValidSite():
    
    while True:
        site = input("Site: ").strip()
        if not site:
            print("❌ Cannot be empty!")
        elif isValidSite(site):
            print(f"✅ {site} verified!")
            return site
        else:
            print(f"❌ '{site}' is not a real site!")

