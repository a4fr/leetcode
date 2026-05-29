# 394. Decode String

class Solution:
    def decode_first_bracket(self, s):
        result = ""
        stack_bracket = []
        
        for i, ch in enumerate(s):
            if ch == "[":
                stack_bracket.append(i)
            elif ch == "]":
                start = stack_bracket.pop()
                num_start = start - 1
                while num_start > 0:
                    if not s[num_start].isdigit():
                        num_start += 1
                        break
                    num_start -= 1
                # print(start, i, "-", int(s[num_start:start]), "X", s[start:i+1])

                if num_start != 0:
                    result += s[:num_start]
                result += int(s[num_start:start]) * s[start+1:i]
                if i < len(s) - 1:
                    result += s[i+1:]
                return result

    def decodeString_approach1(self, s: str) -> str:
        ops = len([1 for ch in s if ch == "["])
        for _ in range(ops):
            s = self.decode_first_bracket(s)
        return s
    
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif ch == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num

            else:
                curr_str += ch
            print(stack, curr_str)
        return curr_str

inputs = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    # ("100[100[100[a]]]", 10**6*"a")
]
s = Solution()
# print(s.decode_first_bracket("aaa2[bc]"))
for string, result in inputs:
    my_result = s.decodeString(string)
    print(my_result, my_result==result)
