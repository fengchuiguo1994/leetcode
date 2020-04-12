## leetcode
the python/C/JAVA code to solve the leetcode problem

#### 1.两数之和-简单（TwoSum-simple）
###### 题目详情
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
###### 题解思路
1：最直接的方式直接双层遍历该数组，找到两个数相加等于该结果。时间复杂度为O(n^2 )。该方法的变种就是遍历一次数组，然后在该数组中搜索target-x是否存在。但是时间复杂度都是O(n^2 )，空间复杂度是T(n)

--------------------------------
2：利用集合或者字典（hash）寻找是否存在的时间复杂度为O(1)的特性。因为该题是返回的索引值，所以只可以用字典，不可以用集合。构建另外一个存储了相同元素的字典，然后判断target-x是不是存在，时间复杂度是先遍历构建字典，然后遍历寻找是否存在O(n)+O(n)+O(1) = O(n)，空间复杂度为数组和字典的键值T(n)+T(n)+T(n) = T(n)

--------------------------------
3：是方法2的改进，可以在构建字典的时候同时判断是否存在。遍历x，判断target-x是否存在，若存在，结束。若不存在，将x存入字典中。

第一种和第二种方法的解是一致的，第三种和前两种可能不一致
```
method1 use time 2.2591547966 s
method1 use time 0.0500032902 s
method1 use time 0.0010178089 s
```

#### 2.两数相加
利用链表实现多位数的相加,难点是控制不等长的链表,然后需要记得进位。时间复杂度是max{O(N),O(M))。所以是O(N)

#### 3. 无重复字符的最长子串
难点,怎么去找到最长的子串,第一种是暴力搜索(不用想了,没通过)。换种思路,我们遍历字符串,每次逐一加一个字符到substring中,然后判断有没有重复的,如果有,记录下当前字串长度,然后就从头开始剔除到这个字符的位置的字符串,然后重复上面的工作。[参考](http://www.luyixian.cn/news_show_11941.aspx)

#### 4. 寻找两个有序数组的中位数
难点:首先要确定中位数是分奇数个和偶数个的,然后用多路归并(两路归并)的算法将两个列表有序整合起来,在对应的位置上获取中位数。

#### 5. 最长回文子串
难点:回文分两种,一种是奇数个的回文,还有一个是偶数个的回文。

#### 6. Z 字形变换
难点:在一个周期里：处于同一行的两个数的位置满足关系(i+j) = 2(numRows-1),该代码是一行一行的遍历整个字符串来实现的,时间复杂度是O(numRows*len(s)),可以考虑一个周期一个周期的处理,这样时间复杂度就是O(len(s))。效率更高

#### 7. 整数反转
在python中实则没有int的限制,但是我们可以人为的限制一下。比较简单,看到了一个比较厉害的C的代码,后面再琢磨一下

#### 8. 字符串转换整数 (atoi)
偷懒用正则表达式提取的数字

#### 9. 回文数
偷懒利用字符串实现,可以考虑一下不用字符串来实现

#### 10. 正则表达式匹配
直接利用正则表达式偷鸡,后面好好的去看看正则表达式的实现

#### 11. 盛最多水的容器
可以用暴力搜索,但是时间复杂度太高。所以换个思路,假设我们从最大的底开始出发,然后我们会有一个面积,然后无论是左边的 +1 右移还是右边的 -1 左移都是为了寻找到一个较高的 高 。当左边不再小于右边的时候结束循环。

#### 12. 整数转罗马数字
开始把题意理解错了,误以为是三位数三位数一个循环,比如：994994,转成罗马数字以为是 CMXCIV CMXCIV。结果后来去查了不对,罗马数字一直到4000000都是不一样的字符表示的(那时候确实没有那么高的生产力),所以代码变成了这样。简单的实现办法是利用 hash 加 贪心 ,将每一个数字对应的罗马数字存储起来,然后从大到小的遍历和目标数进行比较,可以减去的就减,循环到 0 (类似于进制转化,都是贪心的思想)