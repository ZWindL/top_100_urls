import Spliter
import Counter
import MergeSorter

# f_name = input("file name: ")
f_name = './test.txt'
Spliter.split_file(f_name, 10)
Counter.count(10)

tmp_files = []
for i in range(10):
    tmp_files.append('tmp_' + str(i))

file_rst = 'out.txt'
sorter = MergeSorter.LoserTree(tmp_files, 5, file_rst)
sorter.merge()

print('Done, check out file %s' % file_rst)
