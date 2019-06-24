class TmpFile:
    current_line = {'url': '', 'count': 0}
    f_name = ''
    __f__ = object
    eof = False

    def __init__(self, f_name: str):
        self.f_name = f_name
        self.__f__ = open(f_name, 'r')

    def __del__(self):
        self.__f__.close()

    def next_line(self):
        if not self.eof:
            line = self.__f__.readline().replace('\n', '')
            # check if it's eof
            if line == '':
                self.eof = True
                self.current_line = {'url': 'EOF', 'count': -1}
            else:
                line = line.split(' ')
                self.current_line = {'url': line[0], 'count': int(line[1])}
            return self.current_line

    def is_bigger_than(self, another):
        return self.current_line['count'] > another.current_line['count']


class LoserTree:
    tree = []  # loser tree
    tmp_files = []  # file to be merged
    data = []  # leaf nodes
    n = 0  # count of leaf nodes, k of k-ways
    top = 0

    __f_out = object

    # create a loser tree
    def __init__(self, f_names, top, output='out.txt'):
        for f_name in f_names:
            f = TmpFile(f_name)
            self.tmp_files.append(f)
        self.top = top
        # set up output file
        self.__f_out = open(output, 'a')
        self.n = len(self.tmp_files)
        n = self.n
        # set up leaf nodes
        for i in range(n):
            self.data.append(self.tmp_files[i].next_line())
            self.tree.append(-1)
        for i in range(n):
            # n - 1 - i is the last node, because loser tree adjust from bottom to top
            self.adjust(n - 1 - i)

    def __del__(self):
        self.__f_out.close()

    # n is how many ways the program need to merge, s is leaf node
    def adjust(self, s):
        n = self.n
        t = (n + s) // 2
        while t > 0:
            # node which has less count is loser
            if (self.tree[s] != -1 or self.data[self.tree[s]]['count'] > self.data[self.tree[t]]['count']) and s >= 0:
                s, self.tree[t] = self.tree[s], s
            else:
                break
            t = t // 2
        self.tree[0] = s

    # check if sort process is done
    def done(self):
        for f in self.tmp_files:
            if not f.eof:
                return False
        return True

    # write winner into result file
    def write_winner(self):
        data = self.data[self.tree[0]]
        self.__f_out.write(data['url'] + ' ' + str(data['count']) + '\n')

    # merge files into big one
    def merge(self):
        while self.top >= 0 or not self.done():
            self.write_winner()
            # feed next after write
            self.data[self.tree[0]] = self.tmp_files[self.tree[0]].next_line()
            self.adjust(self.tree[0])
            self.top -= 1
