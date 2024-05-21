class StringSearchAlgorithms:
    @staticmethod
    def boyer_moore(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return -1

        last = {}
        for i in range(m):
            last[pattern[i]] = i

        i = m - 1
        k = m - 1
        while i < n:
            if text[i] == pattern[k]:
                if k == 0:
                    return i
                i -= 1
                k -= 1
            else:
                j = last.get(text[i], -1)
                i += m - min(k, j + 1)
                k = m - 1

        return -1

    @staticmethod
    def kmp(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0:
            return -1

        prefix = StringSearchAlgorithms.compute_prefix(pattern)

        q = 0
        for i in range(n):
            while q > 0 and pattern[q] != text[i]:
                q = prefix[q - 1]
            if pattern[q] == text[i]:
                q += 1
            if q == m:
                return i - m + 1

        return -1

    @staticmethod
    def compute_prefix(pattern):
        m = len(pattern)
        prefix = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = prefix[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            prefix[q] = k
        return prefix


import unittest


class TestStringSearchAlgorithms(unittest.TestCase):

    def test_boyer_moore(self):
        text = "ababcababcabc"
        pattern = "abcab"
        self.assertEqual(StringSearchAlgorithms.boyer_moore(text, pattern), 2)

    def test_kmp(self):
        text = "ababcababcabc"
        pattern = "abcab"
        self.assertEqual(StringSearchAlgorithms.kmp(text, pattern), 2)


if __name__ == '__main__':
    unittest.main()
