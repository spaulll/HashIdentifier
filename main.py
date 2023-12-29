import hashid
from pyscript import document


def identify_hash(hash_value):
    # Create a hash identifier object
    identifier = hashid.HashID()
   
    # Identify the hash types
    results = list(identifier.identifyHash(hash_value))
    return results
    # Print the results in a human-readable format
    if results:
        possible_types = ''
        
        for result in results:
            possible_types += f"[+] {result.name}"
            possible_types += "\n"
        return possible_types
    else:
        return None

def findH(event):
    input_hash = document.querySelector("#enteredHash")
    types = identify_hash(str(input_hash))
    if types is None:
        op = f"""
            No hash types identified 😕.
            """
        output_div = document.querySelector("#output")
        output_div.innerText = op
    else:
        op = f"""
            {types}
            """
        output_div = document.querySelector("#output")
        output_div.innerText = op
