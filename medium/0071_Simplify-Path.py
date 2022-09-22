# https://leetcode.com/problems/simplify-path/

from typing import List


class Solution:

    # T = O(N+K), S = O(K)
    #   N - amount of initial symbols in path
    #   K - amount of final entries in path
    def simplify_path(self, path: str) -> str:
        stack: List[str] = list()
        concat = str()
        for symbol in path:
            if symbol == '/':
                self.__process(concat, stack)
                concat = str()
            else:
                concat = concat + symbol
        self.__process(concat, stack)
        canonical = str()
        for item in stack:
            canonical = f'{canonical}/{item}'
        return canonical if canonical else '/'

    # T = O(1), S = O(1)
    def __process(self, concat: str, stack: List[str]) -> None:
        if not concat:
            return
        if concat == '.':
            pass
        elif concat == '..':
            stack.pop() if stack else None
        else:
            stack.append(concat)


if __name__ == '__main__':

    assert Solution().simplify_path('/../')                      == '/'
    assert Solution().simplify_path('/path/to///my/../file.txt') == '/path/to/file.txt'
    assert Solution().simplify_path('///////////')               == '/'
    assert Solution().simplify_path('/./a/..//z/y/././x/')       == '/z/y/x'
