"""
LC 208. Implement Trie (Prefix Tree)
Difficulty: Medium
Tags: Trie, Hash Table, String, Design
Link: https://leetcode.cn/problems/implement-trie-prefix-tree/
Category: 09-graph
"""


# ===== 暴力解法 =====
# 思路: 使用集合存储所有已插入的单词，搜索和前缀检查均使用字符串匹配
# 复杂度: insert O(1), search O(n), startsWith O(n*m) time; O(n*m) space
class TrieBrute:
    def __init__(self):
        # WHY: 使用集合存储所有插入的单词，确保唯一性和O(1)查找
        self.words = set()

    def insert(self, word: str) -> None:
        # WHY: 直接将单词加入集合
        self.words.add(word)

    def search(self, word: str) -> bool:
        # WHY: 直接检查集合中是否存在该单词
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        # WHY: 遍历集合中所有单词，检查是否有以prefix开头的单词
        for word in self.words:
            # WHY: 使用startswith方法检查前缀匹配
            if word.startswith(prefix):
                return True
        # WHY: 未找到匹配的前缀
        return False


# ===== 最优解法 =====
# 思路: 使用字典树（Trie）数据结构，每个节点包含children字典和is_end标志
# 复杂度: insert O(n), search O(n), startsWith O(n) time; O(total_chars) space
class TrieNode:
    # WHY: Trie节点类
    def __init__(self):
        # WHY: children字典存储子节点，键为字符，值为TrieNode对象
        self.children = {}
        # WHY: is_end标志表示从根到当前节点是否构成一个完整的单词
        self.is_end = False


class Trie:
    def __init__(self):
        # WHY: 初始化根节点（空节点，不存储字符）
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # WHY: 从根节点开始遍历
        node = self.root
        # WHY: 逐字符处理单词
        for ch in word:
            # WHY: 如果当前字符不在子节点中，创建新节点
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # WHY: 移动到子节点继续处理下一个字符
            node = node.children[ch]
        # WHY: 标记单词结束
        node.is_end = True

    def search(self, word: str) -> bool:
        # WHY: 从根节点开始遍历
        node = self.root
        # WHY: 逐字符查找
        for ch in word:
            # WHY: 如果某个字符不存在，说明单词不在Trie中
            if ch not in node.children:
                return False
            # WHY: 移动到子节点
            node = node.children[ch]
        # WHY: 检查路径末尾是否为完整单词（而不是前缀）
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # WHY: 从根节点开始遍历
        node = self.root
        # WHY: 逐字符查找前缀
        for ch in prefix:
            # WHY: 如果某个字符不存在，说明前缀不在Trie中
            if ch not in node.children:
                return False
            # WHY: 移动到子节点
            node = node.children[ch]
        # WHY: 只要能完整匹配前缀路径就返回True
        return True


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Implement Trie...")

    # 测试用例1: 标准插入和搜索
    trie1 = Trie()
    trie1.insert("apple")
    assert trie1.search("apple") == True, "search apple 失败"
    assert trie1.search("app") == False, "search app 失败"
    assert trie1.startsWith("app") == True, "startsWith app 失败"
    trie1.insert("app")
    assert trie1.search("app") == True, "search app after insert 失败"
    print("测试用例1通过: apple/app 插入搜索验证")

    # 测试用例2: 暴力解法验证
    trie_brute = TrieBrute()
    trie_brute.insert("hello")
    trie_brute.insert("world")
    assert trie_brute.search("hello") == True, "暴力解法 search hello 失败"
    assert trie_brute.search("world") == True, "暴力解法 search world 失败"
    assert trie_brute.startsWith("hel") == True, "暴力解法 startsWith hel 失败"
    assert trie_brute.startsWith("worl") == True, "暴力解法 startsWith worl 失败"
    assert trie_brute.startsWith("xyz") == False, "暴力解法 startsWith xyz 失败"
    print("测试用例2通过: 暴力解法验证")

    print("All tests passed!")
