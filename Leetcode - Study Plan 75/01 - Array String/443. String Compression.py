# 443. String Compression

class Solution:
    def compress(self, chars: list[str]) -> int:
        compressed = [chars[0], 1]
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                compressed[-1] += 1
            else:
                compressed.extend([chars[i], 1])
        
        result = ""
        for v in compressed:
            if isinstance(v, str):
                result += v
            else:
                if v > 1:
                    result += str(v)

        chars[:] = list(result)
        return len(chars)

inputs = [
    (["a","a","b","b","c","c","c"], 6),
    (["a"], 1),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4),
    (["a","a","b","b","c","c","c"], 6),
    (["a", "a", "b", "c", "c", "c"], 5),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], None),
    (["a","1","<","'","t","<","x","[","S","`"], ["a","1","<","'","t","<","x","[","S","`"]),
]
s = Solution()
for chars, result in inputs:
    my_result = s.compress(chars)
    print(my_result)
    print(chars)