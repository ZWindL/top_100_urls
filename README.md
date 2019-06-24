#Top 100 urls
---

**Unfinished.** Using Loser Tree to merge sorted temp files but I can't fully implement the merge process, there's still lot of issues:
- [ ] Wrong condition in `adjust` method, obviously on comparing, especially when creating loser tree.
- [ ] Because of the first issue, program can only find top 1 most url by frequency correctly
- [ ] Haven't implement multi-thread

###What it does
- [x] Count frequency of urls in every temporary file in which urls are gathered by hash value
- [x] Find the top 1 url with other unstable content and a 'side value': `{'EOF', -1}` which is used to prevent program printing 'side value'

###Conclusion
* I should use more ordinary structure/algorithm such as heap/select sort to merge files instead of unfamiliar algorithms
* C/C++ is more fitable on that problem, python is big resource consumer
* Learn more about algorithm
