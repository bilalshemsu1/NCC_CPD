class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = "".join(map(str, digits))
        digits = int(digits)
        digits = digits+1
        digits = [int(digits) for digits in str(digits)]
        return digits
