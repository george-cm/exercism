def reverse(text):
    reversed = ""
    for c in text:
        reversed = c + reversed
    return reversed
