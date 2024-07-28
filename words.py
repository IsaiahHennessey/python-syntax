def print_upper_words(words, must_start_with):

  for word in words:
    if word[0].lower() in must_start_with:
     print(word.upper())


words = ["Eat", "egal", "eyeball", "page", "toss", "kicker", "Apple", "acorn", "Keeper"]
must_start_with = {'e', 'a','k'}
print_upper_words(words, must_start_with)