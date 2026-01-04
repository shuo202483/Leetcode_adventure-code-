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
