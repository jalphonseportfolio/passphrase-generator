# Passphrase-Generator

My attempt at making security a little less... forgettable. This script generates passphrases using two distinct patterns (Adjective-Noun-Symbol-Number and Verb-Adverb-Symbol-Number) by creatively combining words and symbols. Give it a whirl and boost your memory (and maybe your security!).

This Python script provides a simple and fun way to generate memorable passphrases using two distinct patterns: **Adjective-Noun-Symbol-Number (ajn)** and **Verb-Adverb-Symbol-Number (vas)**. Instead of relying on complex and easily forgotten character combinations, this script leverages the power of familiar words combined with symbols and numbers, making the generated passphrases easier to recall.

## Features

* **Two Passphrase Patterns:**
    * **Adjective-Noun-Symbol-Number (ajn):** Creates passphrases by randomly selecting an adjective, a noun, a symbol, and a number, and joining them with hyphens (e.g., `vibrant-sunset-$-42`). This pattern leverages descriptive language to aid memory.
    * **Verb-Adverb-Symbol-Number (vas):** Generates passphrases by randomly picking a verb, an adverb, a symbol, and a number, connected by hyphens (e.g., `quickly-jumps-@-19`). This pattern uses action-oriented language for better recall.
* **File-Based Word Lists:** The script loads words for each part of the patterns from separate text files (`adjectives.txt`, `nouns.txt`, `verbs.txt`, `adverbs.txt`, `symbols.txt`, `numbers.txt`). This allows for easy customization and expansion of the word and symbol pools. Each word in the text file should be on a new line.
* **Error Handling:** The script includes basic error handling to check if the required word list files are found. If a file is missing, it prints an informative error message and returns an empty list for that word category, preventing the passphrase generation from crashing.
* **User-Friendly Interface:** Upon execution, the script prompts the user to choose between the two passphrase patterns (`ajn` or `vas`). Based on the user's input, it generates and displays a memorable passphrase following the selected pattern. It also provides feedback for invalid choices.
* **Random Selection:** The `random` module is used to ensure that each generated passphrase is unique and unpredictable by randomly selecting words and symbols from the loaded lists.

## How to Use

1.  **Clone the repository** (or download the Python script).
2.  **Create the necessary text files:**
    * `adjectives.txt`: Contains a list of adjectives, one per line.
    * `nouns.txt`: Contains a list of nouns, one per line.
    * `verbs.txt`: Contains a list of verbs, one per line.
    * `adverbs.txt`: Contains a list of adverbs, one per line.
    * `symbols.txt`: Contains a list of symbols (e.g., `@`, `#`, `$`, `%`, `&`, `*`), one per line.
    * `numbers.txt`: Contains a list of numbers (you can have single digits or multi-digit numbers), one per line.
3.  **Populate the text files** with your desired words, symbols, and numbers. The more diverse your lists, the more varied your generated passphrases will be.
4.  **Run the Python script:**
    ```bash
    python your_script_name.py
    ```
5.  **Follow the prompts:** The script will ask you to choose a passphrase pattern (`ajn` or `vas`). Enter your choice and press Enter.
6.  **Your memorable passphrase** will be displayed on the console.

## Customization

* **Word Lists:** You can easily customize the generated passphrases by editing the content of the text files. Add more words, different symbols, or a wider range of numbers to suit your preferences.
* **File Paths:** If you want to use different filenames for your word lists, you can modify the default `filepath` arguments in the `load_words` function and the `adj_file`, `noun_file`, `verb_file`, `adverb_file`, `symbol_file`, and `num_file` arguments in the `generate_patterned_phrase_ajn` and `generate_patterned_phrase_vas` functions.

## Potential Enhancements

* **More Passphrase Patterns:** Adding more creative patterns (e.g., Adverb-Verb-Noun-Number, etc.).
* **Word Filtering:** Implementing options to filter words based on length or other criteria.
* **GUI Interface:** Creating a graphical user interface for easier interaction.
* **Saving Passphrases:** Adding functionality to save generated passphrases securely.
* **Pronounceable Passphrases:** Exploring techniques to generate passphrases that are easier to pronounce.

This script aims to strike a balance between security and memorability, offering a more human-friendly approach to password generation.
