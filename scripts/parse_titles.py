import os
from collections import OrderedDict
current_dir = os.path.dirname(os.path.realpath(__file__))

def get_pairs():
    d = {}
    for filename in os.listdir(os.path.join(current_dir, '../content/post')):
        with open(os.path.join(current_dir, '../content/post', filename)) as f:
            for line in f.readlines():
                if line.startswith('title:'):
                    d[filename] = line.strip().lstrip('title:')
                    break
            else:
                raise 'oh no'
    return d


def get_filenames():
    path = os.path.join(current_dir, 'titles.txt')
    categories = OrderedDict()
    with open(path) as f:
        state = 'OUT'
        category = ''
        for line in f:
            if line.startswith('#'):
                category = line.lstrip('#').strip()
            elif len(line.strip()) == 0:
                pass
            else:
                filename = line.strip().split()[-1]
                fn = os.path.join(current_dir, '../content/post', filename)
                if categories.get(category) is None:
                    categories[category] = []
                categories[category].append(fn)
    return categories

def set_category(category, filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
    contents = [x for x in contents if not x.startswith('juliasections:')]
    contents.insert(2, "juliasections: ['%s']\n" % category);
    with open(filename, 'w') as f:
        f.write(''.join(contents))

def get_diff(categories):
    tagged = set(os.path.basename(x) for vals in categories.values() for x in vals)
    pairs = get_pairs()
    all_files = set(pairs.keys())
    missing = all_files.difference(tagged)
    maxlen = 86
    missing = [(m, pairs[m]) for m in missing]
    missing = sorted(missing, key = lambda x: x[0])
    for filename, title in missing:
        pass
        print "{} {}".format(title.ljust(maxlen, ' '), filename)



if __name__ == "__main__":
    categories = []
    for category, filenames in get_filenames().items():
        for f in filenames:
            set_category(category, f)
        categories.append(category)
    with open('/home/bork/work/homepage/config.yaml') as f:
        contents = f.readlines()
    contents = [x for x in contents if not x.startswith('params') and not x.startswith('  sections') and not x.startswith('  -')]
    contents.append('params:\n')
    contents.append('  sections:\n')
    for c in categories:
        c = c.lower().replace(' ', '-')
        contents.append('  - %s\n' % c)

    with open('/home/bork/work/homepage/config.yaml', 'w') as f:
        f.write(''.join(contents))

    get_diff(get_filenames())
