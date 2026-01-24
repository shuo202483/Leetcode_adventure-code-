class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        s = s.upper().replace('-', '')[::-1]
        res=''
        for i in range(0,len(s),k):
            res+=s[i:i+k]+'-'
        return res[::-1].lstrip('-')

    class Solution:
        def licenseKeyFormatting(self, s: str, k: int) -> str:
            s = s.replace('-', '').upper()[::-1]
            return "-".join((s[i:i+k] for i in range(0,len(s),k))[::-1])


s=Solution()

print(s.licenseKeyFormatting("2-5g-3-J",2))


#逆向思维从后往前推，先满足后面
