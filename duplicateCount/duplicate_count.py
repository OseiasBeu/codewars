def duplicate_count(text):
    # Your code goes here
    countDuplicates = []
    textUpper = text.upper()
    for l in textUpper:
        if textUpper.count(l) > 1:
            if l not in countDuplicates:
                countDuplicates.append(l)    
    return len(countDuplicates)


print(duplicate_count("indivisibility")) #0
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)
# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)