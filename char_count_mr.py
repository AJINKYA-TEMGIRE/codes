from mrjob.job import MRJob

class char_count(MRJob):
    def mapper(self , _ , line):
        for char in line.strip():
            yield char , 1

    def reducer(self , char , count):
        yield char , sum(count)

if __name__ == "__main__":
    char_count.run()