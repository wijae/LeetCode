class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_number_of_bytes(num):
            if (num & int("11111000", 2)) == int("11110000", 2):
                return 4
                
            if (num & int("11110000", 2)) == int("11100000", 2):
                return 3
        
            if (num & int("11100000", 2)) == int("11000000", 2):
                return 2
                
            return 1
        
        def is_following_byte(num):
            return (num & int("11000000", 2)) == int("10000000", 2)
        
        i = 0
        left = 0
        while i < len(data):
            if left == 0:
                if (data[i] & int("11111000", 2)) == int("11111000", 2):
                    return False

                if is_following_byte(data[i]):
                    return False
                
                left = get_number_of_bytes(data[i]) - 1
            else:
                if not(is_following_byte(data[i])):
                    return False
                
                left -= 1
                
            i += 1
                
        return left == 0
        