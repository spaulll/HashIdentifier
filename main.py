import hashid
from pyscript import document


def identify_hash(hash_value):
    try:
        # Create a hash identifier object
        identifier = hashid.HashID()

        # Identify the hash types
        results = list(identifier.identifyHash(hash_value))
    except Exception as e:
        return None

    # Print the results in a human-readable format
    if results:
        possible_types = ''
        for result in results:
            possible_types += f"[+] {result.name}"
            possible_types += "\n"
        return possible_types
    else:
        return None

def findH(evt):
    input_hash = document.querySelector("#input")
    types = identify_hash(str(input_hash.value))
    
    output_div = document.querySelector("#output")
    
    if types is None:
        op = "No hash types found! 😕."
    else:
        document.querySelector("#msg").innerText = "Possible hash types are:\n"
        op = types
       
    
    output_div.innerText = op


def onEnter(evt):
        if evt.key == "Enter":
            findH(evt)