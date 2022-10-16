# https://leetcode.com/problems/word-search/

from typing import List, Set, Tuple


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        track: Set[Tuple[int, int]] = set()
        for i in range(n):
            for j in range(m):
                is_ok = self.__backtrack((i, j), board, word, track)
                assert not track
                if is_ok:
                    return True
        return False

    def __backtrack(self, pose: Tuple[int, int], board: List[List[str]], string: str, track: Set[Tuple[int, int]]) -> bool:
        if not string:
            return True
        n, m = len(board), len(board[0])
        i, j = pose
        if not (0 <= i < n) or not (0 <= j < m):
           return False
        if pose in track:
            return False
        if board[i][j] == string[0]:
            track.add(pose)
        else:
            return False
        is_ok = self.__backtrack((i-1, j), board, string[1:], track) or \
                self.__backtrack((i+1, j), board, string[1:], track) or \
                self.__backtrack((i, j-1), board, string[1:], track) or \
                self.__backtrack((i, j+1), board, string[1:], track)
        track.remove(pose)
        return is_ok


if __name__ == '__main__':

    assert Solution().exist([
        ['A', 'B', 'C'],
        ['D', 'E', 'F']], 'BE')

    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'ABCCED')

    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'SEE')

    assert Solution().exist([
        ['C', 'A', 'A'],
        ['A', 'A', 'A'],
        ['B', 'C', 'D']], 'AAB')

    assert not Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'ABCB')

    assert not Solution().exist([
        ['A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A']], 'AAAAAAAAABAAAAA')
