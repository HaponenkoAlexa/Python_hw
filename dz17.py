def correct_sentence(greetings):
    if not greetings[0].isupper():
        greetings = greetings[0].upper() + greetings[1:]
    if not greetings.endswith('.'):
        greetings += '.'
    return greetings


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
assert correct_sentence("Some. Other. Example") == "Some. Other. Example.", 'Test6'
print('ОК')

