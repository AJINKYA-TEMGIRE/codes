from mrjob.job import MRJob

class word(MRJob):
    def mapper(self , _ , line):
        for word in line.strip().split(" "):
            yield word , 1

    def reducer(self , word , count):
        if word == "I":
            yield word , sum(count)
    
if __name__ == "__main__":
    word.run()

# The names of the functions should be same as mapper and reducer



# with open("wordcount.txt") as f:
#     lines = f.readlines()

# mapped = []
# for i in lines:
#     i = i.strip()
#     for j in i.split(" "):
#         mapped.append((j , 1))

# name = "I"

# count = 0
# print(mapped)

# for i in mapped:
#     if i == (name , 1):
#         count += 1


# print(count)

