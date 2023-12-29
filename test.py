import hashid

def identify_hash(hash_value):
    # Create a hash identifier object
    identifier = hashid.HashID()

    # Identify the hash types
    results = list(identifier.identifyHash(hash_value))

    # Print the results in a human-readable format
    if results:
        possible_types = ''
        
        for result in results:
            possible_types += f"[+] {result.name}"
            possible_types += "\n"
        return possible_types
    else:
        return None
    
print(identify_hash('5d41402abc4b2a76b9719d911017c592'))