## leetcode
the python/JAVA code to solve the leetcode problem

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
在JAVA代码中，实现了shuffle的算法，实际可以用Collections.shuffle()来实现。shuffle算法是从数组末尾开始，末尾的数字出现在任意位置的概率是1/N，倒数第二个出现在任意位置的概率是(N-1)/N * 1/(N-1) = 1/N。

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

#### 7.整数反转-简单（ReverseNumber-simple）
###### 题目详情
给定一个32位的有符号的整数，需要对数字进行反转。123（321）、-123（-321）、120（21）
###### 题解思路
实际上存在反转后溢出的情况。溢出时，返回0。<br/>
1：利用字符串的特性，先判断数字的正负，然后反转字符串，在判断反转后的数字是否越界。

--------------------------------
2：通过取模和取余迅速计算。

这里有几个问题需要注意：<br/>
1：取模取余运算，在JAVA和C中，是用的舍弃小数点的方式，但是在python中却是用的向下取整的方式。在正数运算的场合，结果一致，但是在有负数参与的时候就有不一致。
```
return a-n*int(a/n)  # 取模运算在JAVA和C中
return a-n*int(a/n)  # 在python中

return int(a/n)  # 取余运算在JAVA和C中
return a//n  # 在python中
```
2：JAVA在对int下边界取绝对值的时候不会正确的执行，详见api
```
System.out.println(Math.abs(-2147483648));
-2147483648
```
3：此类问题因为存在固有的界限，实际问题中可能会使用bigNumber模块，突破长度的限制

#### 8. 字符串转换整数 (atoi)
偷懒用正则表达式提取的数字

#### 9.回文数-简单（PalindromeNumber-simple）
###### 题目详情
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。同时也要考虑正负号，所以所有的负数都不可能是回文数
###### 题解思路
1：转化为整型数组或者字符串，依次遍历判断。

--------------------------------
2：直接反转数字，看两次的结果是否相等，直接借用第7题的代码。

#### 10. 正则表达式匹配
直接利用正则表达式偷鸡,后面好好的去看看正则表达式的实现

#### 11. 盛最多水的容器
可以用暴力搜索,但是时间复杂度太高。所以换个思路,假设我们从最大的底开始出发,然后我们会有一个面积,然后无论是左边的 +1 右移还是右边的 -1 左移都是为了寻找到一个较高的 高 。当左边不再小于右边的时候结束循环。

#### 12.13.罗马数字和整数的互换-简单（RomanToInt IntToRoman-simple）
###### 题目详情
将数字转化成罗马数字或者罗马数字转化成整数
###### 题解思路
其实就是个贪心的过程，每次取出最满足条件的那一块完成转化，最后拼接起来

JAVA和python的字符串切片是一致的，都是左闭右开的

#### 14.最长公共前缀唤-简单（LongestCommanPrefix-simple）
###### 题目详情
求一个字符串列表的元素的公共前缀序列
###### 题解思路
1：每次取出第一个元素的第i个位置的字符，然后遍历所有元素的第i个字符，比较是否一致，一致继续，不一致结束。

---
2：在其它地方抄来的一个巧妙办法，利用python的zip的特性一次性取出第i个的字符，然后利用集合迅速判断是否相同。

#### 20.有效的括号-简单（ValidParentheses-simple）
###### 题目详情
判断给定的括号是否都是有效的括号
###### 题解思路
经典的问题，利用栈的入栈和出栈的配对来完成