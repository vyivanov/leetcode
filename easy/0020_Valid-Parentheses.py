# https://leetcode.com/problems/valid-parentheses/

class Solution:

    # T = O(N), S = O(N)
    @staticmethod
    def is_valid(string: str) -> bool:
        assert len(string) > 0
        stack, top = list(), (-1)
        for symbol in string:
            if symbol in '([{':
                stack.append(symbol)
                top = top + 1
            elif symbol in ')]}':
                if not stack:
                    return False
                if stack[top] == '(' and symbol == ')' or \
                   stack[top] == '[' and symbol == ']' or \
                   stack[top] == '{' and symbol == '}':
                    stack.pop()
                    top = top - 1
                else:
                    return False
            else:
                assert False
        return not stack


if __name__ == '__main__':

    assert not Solution.is_valid('[')
    assert not Solution.is_valid(']')
    assert not Solution.is_valid('[({)]')
    assert not Solution.is_valid('[]{}]')

    assert Solution.is_valid('()[]{}')
    assert Solution.is_valid('([{}])')
    assert Solution.is_valid('([{{[]}}])')
