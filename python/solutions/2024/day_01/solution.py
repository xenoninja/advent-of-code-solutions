# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2057374)
    def part_1(self) -> int:
        input_list = self.input
        left_list = []
        right_list = []
        res = 0

        for i in input_list:
            [a, b] = i.split()
            left_list.append(int(a))
            right_list.append(int(b))

        left_list.sort()
        right_list.sort()

        for i in range(len(input_list)):
            res += abs(left_list[i] - right_list[i])

        return res

    @answer(23177084)
    def part_2(self) -> int:
        input_list = self.input
        left_list = []
        count_dict = {}
        res = 0

        for i in input_list:
            [a, b] = i.split()
            left_list.append(int(a))
            count_dict[int(b)] = count_dict.get(int(b), 0) + 1

        for i in left_list:
            if i in count_dict:
                res += count_dict[i] * i

        return res

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
