import json

def loadJson(path):
    with open(path, "r") as f:
        try:
            data = json.load(f)

        except Exception:
            data = []
            writeJson(path, data)

    return data     

def writeJson(path, data):

    with open(path, "w") as f:
        json.dump(data, f)
        print(f"✅ JSON saved successfully to {path} 🎉")