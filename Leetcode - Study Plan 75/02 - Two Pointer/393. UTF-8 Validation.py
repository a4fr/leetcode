# 393. UTF-8 Validation

class Solution:
    def to_8bit(self, data: int) -> str:
        return bin(data)[2:].zfill(8)
    
    def validate_n_byte_utf8(self, arr: list[str]):
        n_byte = len(arr)
        # N = 1
        if n_byte == 1:
            if arr[0][:1] == '0':
                return True
            return False

        # N > 1
        for i, data in enumerate(arr):
            if i == 0 and data[:n_byte+1] != '1'*n_byte+'0':
                return False

            if i > 0 and data[:2] != '10':
                return False
            
        return True

    def validUtf8_approach1(self, data: list[int]) -> bool:
        start = 0
        end = 0
        while start < len(data):
            n = self.to_8bit(data[start]).find('0')
            if n > 4:
                return False
            elif n == -1:
                return False
            elif n == 0:
                end = start
            else:
                end = start + n -1

            if end > len(data) + 1:
                return False
            
            # print(arr[start:end+1])
            if not self.validate_n_byte_utf8([self.to_8bit(num) for num in data[start:end+1]]):
                return False
            
            start = end + 1
        return True
    
    def validUtf8(self, data: list[int]) -> bool:
        n = 1

        for num in data:
            # print(self.to_8bit(num))
            if n == 1:
                if num >> 7 == 0:
                    continue
                elif (num >> 5) == 0b110:
                    n = 2
                elif (num >> 4) == 0b1110:
                    n = 3
                elif (num >> 3) == 0b11110:
                    n = 4
                else:
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                n -= 1
        return n == 1



inputs = [
    ([197,130,1], True),
    ([235,140,4], False),
    ([250,145,145,145,145], False),
    ([240,162,138,147], True),
]
s = Solution()
# print(s.validate_n_byte_utf8(['11000101', '10000010']))
# print(s.validate_n_byte_utf8(['00000001']))
for data, result in inputs:
    my_result = s.validUtf8(data)
    print(my_result, my_result==result)
