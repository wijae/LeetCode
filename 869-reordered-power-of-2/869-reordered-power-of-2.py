class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        l = sorted(list(str(n)))
        l2 = [sorted(list(str(2**i))) for i in range(50)]
        return any([l == ll for ll in l2])
        