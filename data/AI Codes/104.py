import enchant

def spell_checker(word):
    d = enchant.Dict("en_US")
    if d.check(word):
        return f"'{word}' is spelled correctly."
    else:
        return f"'{word}' is misspelled. Suggestions: {', '.join(d.suggest(word))}"

def main():
    print("Spell Checker")
    word = input("Enter a word to check: ")
    result = spell_checker(word)
    print(result)

if __name__ == "__main__":
    main()
