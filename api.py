import httpx

def obfuscate(script):
    url = "https://wearedevs.net/api/obfuscate"

    data = {
        "script": script
    }

    response = httpx.post(url, data=data)
    return response

def inputscript():
    script = input("Enter your script: ")
    return script

def response():
    script = inputscript()
    response = obfuscate(script)
    ofuscated = response.json()
    return ofuscated['obfuscated']