# leetcode
the python/C code to solve the leetcode problem

### 1.两数之和
利用字典记录该列表的元素和位置,然后判断 target-当前元素 存不存在就行,所以至多遍历一次就行,时间复杂度O(n),空间复杂度:列表本身T(n),转成字典2T(n),合计3T(n)即T(n)。<br/>
python:use time 60 ms