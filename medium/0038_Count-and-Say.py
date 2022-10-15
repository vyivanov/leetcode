# https://leetcode.com/problems/count-and-say/


class Solution:

    # T = O(n**2), S = O(n)
    def count_and_say_1(self, n: int) -> str:
        assert 1 <= n <= 30
        return self.__helper('1', n-1)

    # T = O(n**2), S = O(n)
    def __helper(self, string: str, n: int) -> str:
        if not n:
            return string
        saying = str()
        symbol, counter = string[0], 1
        for item in string[1:]:
            if item == symbol:
                counter = counter + 1
            else:
                saying += str(counter) + symbol
                symbol, counter = item, 1
        saying += str(counter) + symbol
        return self.__helper(saying, n-1)

    # T = O(n**2), S = O(n)
    def count_and_say_2(self, n: int) -> str:
        assert 1 <= n <= 30
        string = '1'
        for __ in range(n-1):
            saying = str()
            symbol, counter = string[0], 1
            for item in string[1:]:
                if item == symbol:
                    counter = counter + 1
                else:
                    saying += str(counter) + symbol
                    symbol, counter = item, 1
            string = saying + str(counter) + symbol
        return string


if __name__ == '__main__':

    for pfn in [Solution().count_and_say_1, Solution().count_and_say_2]:

        assert pfn(1) == '1'
        assert pfn(2) == '11'
        assert pfn(3) == '21'
        assert pfn(4) == '1211'
        assert pfn(5) == '111221'
        assert pfn(6) == '312211'
        assert pfn(7) == '13112221'
        assert pfn(8) == '1113213211'
        assert pfn(9) == '31131211131221'
