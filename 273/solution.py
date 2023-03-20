class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        thousands = ['','Thousand','Million','Billion']
        def helper(num):
            if num == 0:
                return ''
            elif num < 20:
                return ones[num] + ' '
            elif num < 100:
                return tens[num//10] + ' ' + helper(num%10)
            else:
                return ones[num//100] + ' Hundred ' + helper(num%100)
        res = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + ' ' + res
            num //= 1000
            i += 1
        return res.strip()