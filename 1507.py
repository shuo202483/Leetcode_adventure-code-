
class Solution:
    def reformatDate(self, date: str) -> str:
        day_part,month_part,year=date.split()

        day=day_part[:-2]
        day=day.zfill(2)
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month = month_map[month_part]

        return f"{year}-{month}-{day}"





s=Solution()
print(s.reformatDate("20th Oct 2052"))

zfill是python一种自动补零的字符串函数功能