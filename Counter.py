import collections


def count(file_count: int, suffix: str = 'tmp_'):
    """count strings in tmp files

    :file_count: how many files to be counted
    :suffix: the suffix of tmp files

    """
    rst = {}
    for c in range(file_count):
        f = open(suffix + str(c), 'r+')
        for key in f:
            if rst.__contains__(key):
                rst[key] += 1
            else:
                rst[key] = 1
        # sort urls in each tmp file with their count
        rst = collections.OrderedDict(sorted(rst.items(), key=lambda kv: kv[1], reverse=True))
        # rst = collections.OrderedDict(sorted(rst, key=lambda kv: kv[1], reverse=True))
        # back to begin of a file and cover the content with <url, count> pair
        f.seek(0)
        f.truncate()
        for k, v in rst.items():
            f.write(k.replace('\n', ' ') + str(v) + '\n')
        f.close()
        rst = {}

