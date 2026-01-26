class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return (s[0]+"*****"+s.split("@")[0][-1]+"@"+s.split("@")[1]).lower()
        else:
            nums=''
            """
            每次 nums += i：字符串拼接，最坏情况下是 O(n^2)，因为 Python 字符串是不可变对象，
            每次拼接都会新建一个字符串，此外种做法还有反转所产生的开销
            """
            for i in s[::-1]:
                if '0' <= i <= '9':
                    nums = nums + i

            n=len(nums)
            if n==10:
                return "***-***-"+nums[::-1][-4:]
            if n==11:
                return "+*-***-***-"+nums[::-1][-4:]
            if n==12:
                return "+**-***-***-"+nums[::-1][-4:]
            if n==13:
                return "+***-***-***"+nums[::-1][-4:]


#优化后的代码
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return (s[0] + "*****" + s.split("@")[0][-1] + "@" + s.split("@")[1]).lower()
        else:
            "这里最多持续5xn次，相比前者省了一个量级"
            for x in ['+', '-', '(', ')', ' ']:
                s = s.replace(x, '')
            # 判断长度
            n = len(s)
            if n == 10:
                # 无国家码
                s = '***-***-' + s[-4:]
            else:
                # 有国家码
                "这里省去了判断和反转"
                s = '+' + ('*' * (n - 10)) + '-***-***-' + s[-4:]
        return s




s=Solution()
print(s.maskPII("AB@qq.com"))
print(s.maskPII("LeetCode@LeetCode.com"))
print(s.maskPII("1(234)567-890"))