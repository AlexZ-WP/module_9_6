
def all_variants(text):
    for r in range(len(text)):
        for j in range(len(text)-r):
            yield text[j:j+r+1]

a = all_variants("abc")
for i in a:
    print(i)