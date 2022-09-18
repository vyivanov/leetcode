# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:

    BUTTONS = {
        '2': 'abc' ,
        '3': 'def' ,
        '4': 'ghi' ,
        '5': 'jkl' ,
        '6': 'mno' ,
        '7': 'pqrs',
        '8': 'tuv' ,
        '9': 'wxyz',
    }

    # T = O(N), S = O(N)
    def letter_combinations(self, digits: str) -> List[str]:
        output: List[str] = list()
        concat = str()
        if len(digits) > 0:
            self.__process(digits, concat, output)
        return output

    # T = O(N), S = O(N)
    def __process(self, digits: str, concat: str, output: List[str]) -> None:
        n = len(digits)
        letters = Solution.BUTTONS[digits[0]]
        for symbol in letters:
            if n > 1:
                self.__process(digits[1:], concat + symbol, output)
            else:
                output.append(concat + symbol)


if __name__ == '__main__':

    assert Solution().letter_combinations(   '') == []
    assert Solution().letter_combinations(  '2') == ['a', 'b', 'c']
    assert Solution().letter_combinations( '23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert Solution().letter_combinations('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi',
                                                     'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi',
                                                     'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
