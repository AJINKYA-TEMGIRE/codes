from mrjob.job import MRJob , MRStep

class mintemp(MRJob):
    def mapper(self , _ , line):
        year , temp = line.strip().split(",")
        yield year , temp

    def reduce_min_temp(self , year , temp):
        min_temp = max(temp)
        yield None , (year , min_temp)

    def reduce_year(self , _ , year):
        min_year = max(year , key = lambda x : x[1])
        yield min_year

    def steps(self):
        return [MRStep(mapper = self.mapper , reducer = self.reduce_min_temp),
                MRStep(reducer = self.reduce_year)]
    
if __name__ == "__main__":
    mintemp.run()
