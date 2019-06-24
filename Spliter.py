def split_file(f_name: str, count: int, suffix='tmp_'):
    """split file into `count` parts by their hash value

    :f_name: file to be read
    :count: how many files to create
    :suffix: suffix of split file

    """
    f = open(f_name, 'r')

    for s in f:
        hash_of_s = hash(s)
        f_out = open(suffix + str(hash_of_s % count), 'a')
        f_out.write(s)
        f_out.close()

    f.close()
