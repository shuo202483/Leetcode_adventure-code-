class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
            #没有学生喜欢该形状的三明值时
            if sandwiches and sandwiches[0] not in students:
                return len(students)
        return 0


#计数的方法完成
class Solution:
    def countStudents(self, students, sandwiches):
        from collections import Counter
        count = Counter(students)
        n = len(sandwiches)

        for i, s in enumerate(sandwiches):
            if count[s] == 0:
                # 没人要这个三明治了，停止
                return n - i
            count[s] -= 1

        return 0
