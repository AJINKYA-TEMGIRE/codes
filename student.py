# class map_reduce:

#     def __init__(self):
#         self.n = int(input("Enter the number of student: "))
#         self.mapper()
#         self.reduce(self.students)

#     def mapper(self) :
#         self.students = []
#         with open("student.txt" , "r") as f:
#             for i in range(self.n):
#                 line = f.readline().strip().split(" ")
#                 line[1] = int(line[1].strip())
#                 self.students.append(line)

#         return self.students
    
#     def reduce(self , s):
        
#         for name , marks in s:
#             grade = ""
#             if marks > 90:
#                 grade = "A"
#             else:
#                 grade = "B"

#             print(name , grade)
            


        

    
# m = map_reduce()


from mrjob.job import MRJob

class grade(MRJob):

    def mapper(self , _ , line):
        name , marks = line.strip().split(" ")
        yield name , int(marks)
    
    def reducer(self , name , marks):
        if sum(marks) > 90:

            yield name, "A"

            # Own logic for grade system


if __name__ == "__main__":
    grade.run()
