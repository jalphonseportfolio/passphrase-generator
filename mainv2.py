import random

def load_words(filepath="wordlist.txt"):
    """Loads words from a text file where each word is on a new line."""
    try:
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []

def generate_patterned_phrase_ajn(adj_file="adjectives.txt", noun_file="nouns.txt", symbol_file="symbols.txt", num_file="numbers.txt"):
    """Generates a passphrase using the Adjective-Noun-Number pattern, loading words from files."""
    adjectives = load_words(adj_file)
    nouns = load_words(noun_file)
    symbol = load_words(symbol_file)
    numbers = load_words(num_file)

    if not adjectives or not nouns or not symbol or not numbers:
        return "Error: Could not load word lists."

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    symbol = random.choice(symbol)
    number = random.choice(numbers)
    return f"{adjective}-{noun}-{symbol}-{number}"

def generate_patterned_phrase_vas(verb_file="verbs.txt", adverb_file="adverbs.txt", symbol_file="symbols.txt", num_file="numbers.txt"):
    """Generates a passphrase using the Verb-Adverb-Symbol pattern, loading words from files."""
    verbs = load_words(verb_file)
    adverbs = load_words(adverb_file)
    symbol = load_words(symbol_file)
    numbers = load_words(num_file)

    if not verbs or not adverbs or not symbol or not numbers:
        return "Error: Could not load word lists."

    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    symbol = random.choice(symbol)
    number = random.choice(numbers)
    return f"{verb}-{adverb}-{symbol}-{number}"

print("Welcome to the Memorable Passphrase Generator!")
pattern_choice = input("Choose a pattern (ajn for Adjective-Noun-Symbol-Number, vas for Verb-Adverb-Symbol-Number): ").lower()

if pattern_choice == "ajn":
    memorable_passphrase = generate_patterned_phrase_ajn()
    print("Your memorable passphrase (Adjective-Noun-Symbol-Number):", memorable_passphrase)
elif pattern_choice == "vas":
    memorable_passphrase = generate_patterned_phrase_vas()
    print("Your memorable passphrase (Verb-Adverb-Symbol-Number):", memorable_passphrase)
else:
    print("Invalid pattern choice. Please choose 'ajn' or 'vas'.")