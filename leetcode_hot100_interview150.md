# LeetCode Hot 100 × 面试经典 150：去重复习清单

> 资料范围：力扣的 [Hot 100](https://leetcode.cn/studyplan/top-100-liked/) 与[面试经典 150](https://leetcode.cn/studyplan/top-interview-150/)。
>
> 题单成员资格以用户于 2026-07-29 从上述两个官方页面复制的标题清单为准；不再从其他题单补题。按**核心解法模式**归类；同一题只归入最值得复习的模式，组内按 LeetCode 原始题号升序。题名链接到题目，`Py` 链接到可运行的 Python 参考实现（用于对照；先独立完成再打开）。

## 使用方式

1. 先遮住“核心模板”，限时 20–35 分钟独立写出。
2. 卡住时只看模板与复杂度；仍不能完成再看 `Py`。
3. 每次复习只重写模板，不背完整代码。链表/树题在本地补上 `ListNode` / `TreeNode` 定义即可运行。

## 哈希、计数与前缀和

核心模板：`dict/set` 做 O(1) 查找；前缀和记录“某个和首次/出现次数”。

- [1. 两数之和](https://leetcode.cn/problems/two-sum/) · [Py](https://walkccc.me/LeetCode/problems/0001/) — 哈希表互补数，O(n)/O(n)
- [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/) · [Py](https://walkccc.me/LeetCode/problems/0049/) — 排序键或 26 位计数键，O(n·k log k)
- [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) · [Py](https://walkccc.me/LeetCode/problems/0128/) — 只从序列起点向后扩展，O(n)
- [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/) · [Py](https://walkccc.me/LeetCode/problems/0136/) — XOR 抵消，O(n)/O(1)
- [169. 多数元素](https://leetcode.cn/problems/majority-element/) · [Py](https://walkccc.me/LeetCode/problems/0169/) — Boyer-Moore 投票，O(n)/O(1)
- [202. 快乐数](https://leetcode.cn/problems/happy-number/) · [Py](https://walkccc.me/LeetCode/problems/0202/) — 集合判环，O(log n)
- [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings/) · [Py](https://walkccc.me/LeetCode/problems/0205/) — 双向映射，O(n)
- [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/) · [Py](https://walkccc.me/LeetCode/problems/0219/) — 最近下标哈希，O(n)
- [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/) · [Py](https://walkccc.me/LeetCode/problems/0242/) — 频次计数，O(n)
- [290. 单词规律](https://leetcode.cn/problems/word-pattern/) · [Py](https://walkccc.me/LeetCode/problems/0290/) — 双射，O(n)
- [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) · [Py](https://walkccc.me/LeetCode/problems/0347/) — 频次 + 桶，O(n)
- [383. 赎金信](https://leetcode.cn/problems/ransom-note/) · [Py](https://walkccc.me/LeetCode/problems/0383/) — 库存扣减，O(n)
- [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) · [Py](https://walkccc.me/LeetCode/problems/0560/) — 前缀和频次，O(n)

## 双指针、原地数组与区间

核心模板：有序数组从两端收缩；原地题用写指针；区间题先按端点排序。

- [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) · [Py](https://walkccc.me/LeetCode/problems/0011/) — 短板移动，O(n)
- [15. 三数之和](https://leetcode.cn/problems/3sum/) · [Py](https://walkccc.me/LeetCode/problems/0015/) — 排序 + 夹逼去重，O(n²)
- [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) · [Py](https://walkccc.me/LeetCode/problems/0026/) — 快慢指针，O(n)/O(1)
- [27. 移除元素](https://leetcode.cn/problems/remove-element/) · [Py](https://walkccc.me/LeetCode/problems/0027/) — 写指针过滤，O(n)/O(1)
- [31. 下一个排列](https://leetcode.cn/problems/next-permutation/) · [Py](https://walkccc.me/LeetCode/problems/0031/) — 找降序边界、交换、反转，O(n)
- [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/) · [Py](https://walkccc.me/LeetCode/problems/0041/) — 下标原地哈希，O(n)/O(1)
- [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) · [Py](https://walkccc.me/LeetCode/problems/0042/) — 两端维护左右最高，O(n)/O(1)
- [56. 合并区间](https://leetcode.cn/problems/merge-intervals/) · [Py](https://walkccc.me/LeetCode/problems/0056/) — 排序后贪心合并，O(n log n)
- [57. 插入区间](https://leetcode.cn/problems/insert-interval/) · [Py](https://walkccc.me/LeetCode/problems/0057/) — 三段扫描，O(n)
- [75. 颜色分类](https://leetcode.cn/problems/sort-colors/) · [Py](https://walkccc.me/LeetCode/problems/0075/) — 荷兰国旗三指针，O(n)
- [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/) · [Py](https://walkccc.me/LeetCode/problems/0080/) — 保留两次的写指针，O(n)
- [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) · [Py](https://walkccc.me/LeetCode/problems/0088/) — 从尾部回填，O(m+n)
- [125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/) · [Py](https://walkccc.me/LeetCode/problems/0125/) — 两端跳过非字母数字，O(n)
- [167. 两数之和 II](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) · [Py](https://walkccc.me/LeetCode/problems/0167/) — 有序夹逼，O(n)
- [189. 轮转数组](https://leetcode.cn/problems/rotate-array/) · [Py](https://walkccc.me/LeetCode/problems/0189/) — 三次反转，O(n)/O(1)
- [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/) · [Py](https://walkccc.me/LeetCode/problems/0228/) — 连续段扫描，O(n)
- [240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) · [Py](https://walkccc.me/LeetCode/problems/0240/) — 右上角消去一行/列，O(m+n)
- [283. 移动零](https://leetcode.cn/problems/move-zeroes/) · [Py](https://walkccc.me/LeetCode/problems/0283/) — 非零写指针，O(n)
- [392. 判断子序列](https://leetcode.cn/problems/is-subsequence/) · [Py](https://walkccc.me/LeetCode/problems/0392/) — 前进匹配，O(n)
- [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) · [Py](https://walkccc.me/LeetCode/problems/0452/) — 按右端点选点，O(n log n)

## 滑动窗口

核心模板：右指针扩张，违反约束时左指针收缩；计数表只维护窗口内状态。

- [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) · [Py](https://walkccc.me/LeetCode/problems/0003/) — 最近位置跳左边界，O(n)
- [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) · [Py](https://walkccc.me/LeetCode/problems/0076/) — 满足覆盖后尽量缩窗，O(n)
- [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/) · [Py](https://walkccc.me/LeetCode/problems/0209/) — 正数和的可收缩窗口，O(n)
- [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) · [Py](https://walkccc.me/LeetCode/problems/0239/) — 单调递减队列，O(n)
- [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) · [Py](https://walkccc.me/LeetCode/problems/0438/) — 定长窗口计数，O(n)

## 栈、单调栈与表达式

核心模板：栈保存“尚未匹配/尚未结算”的状态；单调栈弹出时结算答案。

- [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/) · [Py](https://walkccc.me/LeetCode/problems/0020/) — 括号配对栈，O(n)
- [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/) · [Py](https://walkccc.me/LeetCode/problems/0032/) — 下标哨兵栈，O(n)
- [71. 简化路径](https://leetcode.cn/problems/simplify-path/) · [Py](https://walkccc.me/LeetCode/problems/0071/) — 路径分段栈，O(n)
- [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) · [Py](https://walkccc.me/LeetCode/problems/0084/) — 单调递增栈，O(n)
- [150. 逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) · [Py](https://walkccc.me/LeetCode/problems/0150/) — 操作数栈，O(n)
- [155. 最小栈](https://leetcode.cn/problems/min-stack/) · [Py](https://walkccc.me/LeetCode/problems/0155/) — 同步最小值栈，O(1)/操作
- [224. 基本计算器](https://leetcode.cn/problems/basic-calculator/) · [Py](https://walkccc.me/LeetCode/problems/0224/) — 符号与括号上下文栈，O(n)
- [394. 字符串解码](https://leetcode.cn/problems/decode-string/) · [Py](https://walkccc.me/LeetCode/problems/0394/) — 数字/字符串栈，O(n)
- [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/) · [Py](https://walkccc.me/LeetCode/problems/0739/) — 等待更大值的下标栈，O(n)

## 链表

核心模板：虚拟头简化边界；快慢指针找中点/环；反转以 `prev, cur, nxt` 三变量推进。

- [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/) · [Py](https://walkccc.me/LeetCode/problems/0002/) — 逐位进位，O(n)
- [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) · [Py](https://walkccc.me/LeetCode/problems/0019/) — 固定间隔双指针，O(n)
- [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) · [Py](https://walkccc.me/LeetCode/problems/0021/) — 哨兵归并，O(m+n)
- [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) · [Py](https://walkccc.me/LeetCode/problems/0023/) — 最小堆多路归并，O(n log k)
- [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) · [Py](https://walkccc.me/LeetCode/problems/0024/) — 前驱重连，O(n)
- [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/) · [Py](https://walkccc.me/LeetCode/problems/0025/) — 分组检查后局部反转，O(n)
- [61. 旋转链表](https://leetcode.cn/problems/rotate-list/) · [Py](https://walkccc.me/LeetCode/problems/0061/) — 成环后断开，O(n)
- [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/) · [Py](https://walkccc.me/LeetCode/problems/0082/) — 哨兵跳过整段重复，O(n)
- [86. 分隔链表](https://leetcode.cn/problems/partition-list/) · [Py](https://walkccc.me/LeetCode/problems/0086/) — 两条链拼接，O(n)
- [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) · [Py](https://walkccc.me/LeetCode/problems/0092/) — 头插法局部反转，O(n)
- [138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/) · [Py](https://walkccc.me/LeetCode/problems/0138/) — 原链交织复制，O(n)/O(1)
- [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/) · [Py](https://walkccc.me/LeetCode/problems/0141/) — Floyd 快慢指针，O(n)/O(1)
- [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) · [Py](https://walkccc.me/LeetCode/problems/0142/) — 相遇后同速找入口，O(n)/O(1)
- [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/) · [Py](https://walkccc.me/LeetCode/problems/0146/) — 哈希表 + 双向链表，O(1)/操作
- [148. 排序链表](https://leetcode.cn/problems/sort-list/) · [Py](https://walkccc.me/LeetCode/problems/0148/) — 自底向上归并，O(n log n)
- [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) · [Py](https://walkccc.me/LeetCode/problems/0160/) — 切换链表头抵消长度差，O(n)
- [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/) · [Py](https://walkccc.me/LeetCode/problems/0206/) — 三指针迭代，O(n)/O(1)
- [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/) · [Py](https://walkccc.me/LeetCode/problems/0234/) — 找中点、反转后半、比较，O(n)/O(1)

## 二分查找与答案二分

核心模板：明确单调谓词，维护闭区间；旋转数组先判断哪一半有序。

- [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/) · [Py](https://walkccc.me/LeetCode/problems/0004/) — 较短数组二分分割，O(log min(m,n))
- [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/) · [Py](https://walkccc.me/LeetCode/problems/0033/) — 判断有序半边，O(log n)
- [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) · [Py](https://walkccc.me/LeetCode/problems/0034/) — 两次 lower bound，O(log n)
- [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/) · [Py](https://walkccc.me/LeetCode/problems/0035/) — lower bound，O(log n)
- [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/) · [Py](https://walkccc.me/LeetCode/problems/0074/) — 二维映射一维，O(log mn)
- [153. 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) · [Py](https://walkccc.me/LeetCode/problems/0153/) — 与右端比较，O(log n)
- [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/) · [Py](https://walkccc.me/LeetCode/problems/0162/) — 上坡方向必有峰，O(log n)
- [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/) · [Py](https://walkccc.me/LeetCode/problems/0287/) — 值域二分或 Floyd，O(n log n)/O(1)

## 树：遍历、BST 与路径

核心模板：递归返回子问题信息；BST 用上下界或中序性质；层序遍历用队列分层。

- [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) · [Py](https://walkccc.me/LeetCode/problems/0094/) — 显式栈模拟递归，O(n)
- [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/) · [Py](https://walkccc.me/LeetCode/problems/0098/) — 递归上下界，O(n)
- [100. 相同的树](https://leetcode.cn/problems/same-tree/) · [Py](https://walkccc.me/LeetCode/problems/0100/) — 同步 DFS，O(n)
- [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/) · [Py](https://walkccc.me/LeetCode/problems/0101/) — 镜像 DFS，O(n)
- [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) · [Py](https://walkccc.me/LeetCode/problems/0102/) — 队列按层取数，O(n)
- [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) · [Py](https://walkccc.me/LeetCode/problems/0103/) — BFS 分层交替取向，O(n)
- [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) · [Py](https://walkccc.me/LeetCode/problems/0104/) — 后序高度，O(n)
- [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) · [Py](https://walkccc.me/LeetCode/problems/0105/) — 位置哈希 + 区间递归，O(n)
- [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) · [Py](https://walkccc.me/LeetCode/problems/0106/) — 位置哈希 + 区间递归，O(n)
- [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) · [Py](https://walkccc.me/LeetCode/problems/0108/) — 中点递归，O(n)
- [112. 路径总和](https://leetcode.cn/problems/path-sum/) · [Py](https://walkccc.me/LeetCode/problems/0112/) — 递归扣减目标，O(n)
- [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) · [Py](https://walkccc.me/LeetCode/problems/0114/) — 逆前序维护前驱，O(n)
- [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) · [Py](https://walkccc.me/LeetCode/problems/0117/) — 利用 next 串联下一层，O(n)/O(1)
- [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) · [Py](https://walkccc.me/LeetCode/problems/0124/) — 向上只返回单支贡献，O(n)
- [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) · [Py](https://walkccc.me/LeetCode/problems/0129/) — 前缀数字 DFS，O(n)
- [173. 二叉搜索树迭代器](https://leetcode.cn/problems/binary-search-tree-iterator/) · [Py](https://walkccc.me/LeetCode/problems/0173/) — 延迟压左链，均摊 O(1)
- [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) · [Py](https://walkccc.me/LeetCode/problems/0199/) — 层序最后一个，O(n)
- [222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/) · [Py](https://walkccc.me/LeetCode/problems/0222/) — 比较左右高度，O(log²n)
- [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) · [Py](https://walkccc.me/LeetCode/problems/0226/) — 递归交换孩子，O(n)
- [230. 二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) · [Py](https://walkccc.me/LeetCode/problems/0230/) — 中序第 k 个，O(h+k)
- [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) · [Py](https://walkccc.me/LeetCode/problems/0236/) — 后序汇总命中，O(n)
- [427. 建立四叉树](https://leetcode.cn/problems/construct-quad-tree/) · [Py](https://walkccc.me/LeetCode/problems/0427/) — 区域统一则成叶子，O(n²)
- [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/) · [Py](https://walkccc.me/LeetCode/problems/0437/) — 前缀和 DFS，O(n)
- [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/) · [Py](https://walkccc.me/LeetCode/problems/0530/) — 中序相邻差，O(n)
- [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) · [Py](https://walkccc.me/LeetCode/problems/0543/) — 后序高度更新直径，O(n)
- [637. 二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) · [Py](https://walkccc.me/LeetCode/problems/0637/) — BFS 分层求均值，O(n)

## 图、网格 DFS/BFS 与拓扑排序

核心模板：网格题访问即标记；最短步数用 BFS；依赖关系用入度拓扑或三色 DFS。

- [127. 单词接龙](https://leetcode.cn/problems/word-ladder/) · [Py](https://walkccc.me/LeetCode/problems/0127/) — 模式桶 BFS，O(N·L²)
- [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) · [Py](https://walkccc.me/LeetCode/problems/0130/) — 从边界反向标记，O(mn)
- [133. 克隆图](https://leetcode.cn/problems/clone-graph/) · [Py](https://walkccc.me/LeetCode/problems/0133/) — 旧到新映射 DFS，O(V+E)
- [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/) · [Py](https://walkccc.me/LeetCode/problems/0200/) — 淹没连通块，O(mn)
- [207. 课程表](https://leetcode.cn/problems/course-schedule/) · [Py](https://walkccc.me/LeetCode/problems/0207/) — 入度拓扑判环，O(V+E)
- [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/) · [Py](https://walkccc.me/LeetCode/problems/0210/) — 拓扑输出序列，O(V+E)
- [399. 除法求值](https://leetcode.cn/problems/evaluate-division/) · [Py](https://walkccc.me/LeetCode/problems/0399/) — 带权图 DFS，O(V+E)/查询
- [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/) · [Py](https://walkccc.me/LeetCode/problems/0433/) — 枚举单字符 BFS，O(8·4·L)
- [909. 蛇梯棋](https://leetcode.cn/problems/snakes-and-ladders/) · [Py](https://walkccc.me/LeetCode/problems/0909/) — 编号转换 + BFS，O(n²)
- [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/) · [Py](https://walkccc.me/LeetCode/problems/0994/) — 多源 BFS 分钟层，O(mn)

## 回溯与 Trie

核心模板：递归函数只决定当前位置；进入时选择、返回时撤销。Trie 在“很多前缀查询”时替代逐词扫描。

- [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) · [Py](https://walkccc.me/LeetCode/problems/0017/) — 位置递归枚举，O(4ⁿ)
- [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/) · [Py](https://walkccc.me/LeetCode/problems/0022/) — 左右数量约束，Catalan(n)
- [39. 组合总和](https://leetcode.cn/problems/combination-sum/) · [Py](https://walkccc.me/LeetCode/problems/0039/) — 起点防重的选/不选，指数级
- [46. 全排列](https://leetcode.cn/problems/permutations/) · [Py](https://walkccc.me/LeetCode/problems/0046/) — used 数组/交换，O(n·n!)
- [51. N 皇后](https://leetcode.cn/problems/n-queens/) · [Py](https://walkccc.me/LeetCode/problems/0051/) — 列与对角线集合，O(n!)
- [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/) · [Py](https://walkccc.me/LeetCode/problems/0052/) — 同上只计数
- [77. 组合](https://leetcode.cn/problems/combinations/) · [Py](https://walkccc.me/LeetCode/problems/0077/) — 递增起点，O(C(n,k))
- [78. 子集](https://leetcode.cn/problems/subsets/) · [Py](https://walkccc.me/LeetCode/problems/0078/) — 选/不选或逐层扩展，O(n·2ⁿ)
- [79. 单词搜索](https://leetcode.cn/problems/word-search/) · [Py](https://walkccc.me/LeetCode/problems/0079/) — 网格回溯原地标记，O(mn·4ᴸ)
- [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/) · [Py](https://walkccc.me/LeetCode/problems/0131/) — 分割点 DFS + 回文判断，指数级
- [208. 实现 Trie（前缀树）](https://leetcode.cn/problems/implement-trie-prefix-tree/) · [Py](https://walkccc.me/LeetCode/problems/0208/) — children + is_end，O(L)/操作
- [211. 添加与搜索单词](https://leetcode.cn/problems/design-add-and-search-words-data-structure/) · [Py](https://walkccc.me/LeetCode/problems/0211/) — `.` 时分支 DFS，最坏指数级
- [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/) · [Py](https://walkccc.me/LeetCode/problems/0212/) — Trie 剪枝网格 DFS，O(mn·4ᴸ)

## 堆、优先队列与多路归并

核心模板：堆顶永远是“下一步最该处理”的候选；Python `heapq` 是最小堆。

- [215. 数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) · [Py](https://walkccc.me/LeetCode/problems/0215/) — 维护 k 大小最小堆，O(n log k)
- [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/) · [Py](https://walkccc.me/LeetCode/problems/0295/) — 大根堆 + 小根堆，O(log n)/插入
- [373. 查找和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) · [Py](https://walkccc.me/LeetCode/problems/0373/) — 行首入堆扩展，O(k log min(k,m))
- [502. IPO](https://leetcode.cn/problems/ipo/) · [Py](https://walkccc.me/LeetCode/problems/0502/) — 可做项目入大根堆，O(n log n)

## 贪心与 Kadane

核心模板：先找局部选择的单调不劣性；子数组最大和只保留“以当前位置结尾的最佳状态”。

- [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) · [Py](https://walkccc.me/LeetCode/problems/0045/) — 当前层最远覆盖，O(n)
- [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/) · [Py](https://walkccc.me/LeetCode/problems/0053/) — Kadane，O(n)/O(1)
- [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/) · [Py](https://walkccc.me/LeetCode/problems/0055/) — 维护最远可达，O(n)
- [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) · [Py](https://walkccc.me/LeetCode/problems/0121/) — 维护历史最低价，O(n)
- [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) · [Py](https://walkccc.me/LeetCode/problems/0122/) — 累计所有正差，O(n)
- [134. 加油站](https://leetcode.cn/problems/gas-station/) · [Py](https://walkccc.me/LeetCode/problems/0134/) — 总量判定 + 失败后重置起点，O(n)
- [135. 分发糖果](https://leetcode.cn/problems/candy/) · [Py](https://walkccc.me/LeetCode/problems/0135/) — 双向贪心，O(n)
- [274. H 指数](https://leetcode.cn/problems/h-index/) · [Py](https://walkccc.me/LeetCode/problems/0274/) — 桶计数逆扫，O(n)
- [416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/) · [Py](https://walkccc.me/LeetCode/problems/0416/) — 0/1 背包（非贪心），O(n·sum)
- [763. 划分字母区间](https://leetcode.cn/problems/partition-labels/) · [Py](https://walkccc.me/LeetCode/problems/0763/) — 扩张到最远末次出现，O(n)
- [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/) · [Py](https://walkccc.me/LeetCode/problems/0918/) — 最大子段或总和减最小子段，O(n)

## 动态规划

核心模板：先定义 `dp[i]`/`dp[i][j]` 的语义，再列出最后一步的转移；空间压缩只在理解状态后使用。

- [62. 不同路径](https://leetcode.cn/problems/unique-paths/) · [Py](https://walkccc.me/LeetCode/problems/0062/) — 网格路径计数，O(mn)
- [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/) · [Py](https://walkccc.me/LeetCode/problems/0063/) — 障碍置零的路径 DP，O(mn)
- [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/) · [Py](https://walkccc.me/LeetCode/problems/0064/) — 上/左最优，O(mn)
- [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/) · [Py](https://walkccc.me/LeetCode/problems/0070/) — Fibonacci，O(n)/O(1)
- [72. 编辑距离](https://leetcode.cn/problems/edit-distance/) · [Py](https://walkccc.me/LeetCode/problems/0072/) — 插删改三转移，O(mn)
- [97. 交错字符串](https://leetcode.cn/problems/interleaving-string/) · [Py](https://walkccc.me/LeetCode/problems/0097/) — 二维前缀可达，O(mn)
- [118. 杨辉三角](https://leetcode.cn/problems/pascals-triangle/) · [Py](https://walkccc.me/LeetCode/problems/0118/) — 逐行递推，O(n²)
- [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/) · [Py](https://walkccc.me/LeetCode/problems/0120/) — 自底向上，O(n²)
- [123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) · [Py](https://walkccc.me/LeetCode/problems/0123/) — 交易次数状态 DP，O(n)
- [139. 单词拆分](https://leetcode.cn/problems/word-break/) · [Py](https://walkccc.me/LeetCode/problems/0139/) — 前缀可达，O(n²)
- [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/) · [Py](https://walkccc.me/LeetCode/problems/0152/) — 同时维护最大/最小积，O(n)
- [188. 买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) · [Py](https://walkccc.me/LeetCode/problems/0188/) — k 次交易状态 DP，O(nk)
- [198. 打家劫舍](https://leetcode.cn/problems/house-robber/) · [Py](https://walkccc.me/LeetCode/problems/0198/) — 取与不取，O(n)/O(1)
- [221. 最大正方形](https://leetcode.cn/problems/maximal-square/) · [Py](https://walkccc.me/LeetCode/problems/0221/) — 左上三邻居最小值，O(mn)
- [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/) · [Py](https://walkccc.me/LeetCode/problems/0279/) — 完全背包最少数，O(n√n)
- [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) · [Py](https://walkccc.me/LeetCode/problems/0300/) — tails + 二分，O(n log n)
- [322. 零钱兑换](https://leetcode.cn/problems/coin-change/) · [Py](https://walkccc.me/LeetCode/problems/0322/) — 完全背包最小值，O(amount·n)
- [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) · [Py](https://walkccc.me/LeetCode/problems/1143/) — 匹配/跳过转移，O(mn)

## 位运算、数学与字符串模拟

- [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) · [Py](https://walkccc.me/LeetCode/problems/0005/) — 中心扩展，O(n²)
- [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/) · [Py](https://walkccc.me/LeetCode/problems/0006/) — 行号往返模拟，O(n)
- [9. 回文数](https://leetcode.cn/problems/palindrome-number/) · [Py](https://walkccc.me/LeetCode/problems/0009/) — 反转后一半，O(log n)
- [12. 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/) · [Py](https://walkccc.me/LeetCode/problems/0012/) — 贪心枚举符号，O(1)
- [13. 罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/) · [Py](https://walkccc.me/LeetCode/problems/0013/) — 小于右侧则减，O(n)
- [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/) · [Py](https://walkccc.me/LeetCode/problems/0050/) — 快速幂，O(log n)
- [66. 加一](https://leetcode.cn/problems/plus-one/) · [Py](https://walkccc.me/LeetCode/problems/0066/) — 末位进位，O(n)
- [67. 二进制求和](https://leetcode.cn/problems/add-binary/) · [Py](https://walkccc.me/LeetCode/problems/0067/) — 逐位进位，O(n)
- [69. x 的平方根](https://leetcode.cn/problems/sqrtx/) · [Py](https://walkccc.me/LeetCode/problems/0069/) — 整数二分，O(log x)
- [137. 只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/) · [Py](https://walkccc.me/LeetCode/problems/0137/) — 位计数，O(n)
- [149. 直线上最多的点数](https://leetcode.cn/problems/max-points-on-a-line/) · [Py](https://walkccc.me/LeetCode/problems/0149/) — 约分斜率哈希，O(n²)
- [172. 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/) · [Py](https://walkccc.me/LeetCode/problems/0172/) — 统计因子 5，O(log₅n)
- [190. 颠倒二进制位](https://leetcode.cn/problems/reverse-bits/) · [Py](https://walkccc.me/LeetCode/problems/0190/) — 固定 32 位移位，O(1)
- [191. 位 1 的个数](https://leetcode.cn/problems/number-of-1-bits/) · [Py](https://walkccc.me/LeetCode/problems/0191/) — `n &= n-1`，O(popcount)
- [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/) · [Py](https://walkccc.me/LeetCode/problems/0201/) — 消去变化低位，O(log n)

## 数组与矩阵补充（模拟 / 原地变换）

- [14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/) · [Py](https://walkccc.me/LeetCode/problems/0014/) — 逐列/逐串收缩，O(S)
- [28. 找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) · [Py](https://walkccc.me/LeetCode/problems/0028/) — KMP 或内置查找，O(n+m)
- [30. 串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) · [Py](https://walkccc.me/LeetCode/problems/0030/) — 分偏移定长窗口，O(n·L)
- [36. 有效的数独](https://leetcode.cn/problems/valid-sudoku/) · [Py](https://walkccc.me/LeetCode/problems/0036/) — 行列宫集合，O(1)
- [48. 旋转图像](https://leetcode.cn/problems/rotate-image/) · [Py](https://walkccc.me/LeetCode/problems/0048/) — 转置再反转，O(n²)/O(1)
- [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) · [Py](https://walkccc.me/LeetCode/problems/0054/) — 四边界收缩，O(mn)
- [58. 最后一个单词的长度](https://leetcode.cn/problems/length-of-last-word/) · [Py](https://walkccc.me/LeetCode/problems/0058/) — 尾部逆扫，O(n)
- [68. 文本左右对齐](https://leetcode.cn/problems/text-justification/) · [Py](https://walkccc.me/LeetCode/problems/0068/) — 按词贪心填行，O(S)
- [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/) · [Py](https://walkccc.me/LeetCode/problems/0073/) — 首行首列作标记，O(mn)/O(1)
- [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/) · [Py](https://walkccc.me/LeetCode/problems/0151/) — 分词反转，O(n)
- [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/) · [Py](https://walkccc.me/LeetCode/problems/0238/) — 前后缀积，O(n)/O(1) 额外空间
- [289. 生命游戏](https://leetcode.cn/problems/game-of-life/) · [Py](https://walkccc.me/LeetCode/problems/0289/) — 原地编码旧/新状态，O(mn)
- [380. O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/) · [Py](https://walkccc.me/LeetCode/problems/0380/) — 数组 + 值到下标哈希，O(1)/操作

## 复核记录

以下题目也在你提供的两份官方题单中；先补入清单，后续会合并进上方对应考点小节：


本文以题目原始编号作为唯一键，避免同题在不同知识点下重复计数。上面的 `Py` 参考按编号固定，便于后续替换为自己的提交代码。
