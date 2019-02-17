import os
os.chdir('content/post')

from parse_titles import get_pairs

titles = list(reversed(sorted(get_pairs(), key=lambda x: x[0])))
maxlen = max([len(x) for x, _ in titles])
for filename, title in titles:
    print "{} {}".format(title.ljust(maxlen, ' '), filename)
