txt = input()

# unique_symbols = set()
# for ch in txt:
#     unique_symbols.add(ch)

unique_symbols = sorted(set(txt))

for ch in unique_symbols:
    print(f"{ch}: {txt.count(ch)} time/s")