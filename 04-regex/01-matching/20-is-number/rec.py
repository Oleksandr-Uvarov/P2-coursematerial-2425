import pandas as pd

data = {"Emma": 5000, "Oleksandr": 1000}

df = pd.Series(data)

print(df.iloc[0])

xs = [11, 14, 24, 42]
ys = [7, 4, 2]

lst = [[x + y for y in ys] for x in xs]

print(lst)


# 1. dunder
# 2. animal, cat
# 3. square without method from shape (abstract)
# 4. animal, cat, error because no parameter 4 legs
# 5. 
# 6.
# 7. generalization
# 8. comprehension
# 9. yield
# 10. lambda person : person.length
# 11. pd.Series
# 12. pd.DataFrame
