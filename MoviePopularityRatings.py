from mrjob.job import MRJob
from mrjob.step import MRStep

class MoviePopularityRatings(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_sorted_ratings)

        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sorted_ratings(self, count, movies):
        for movie in movies:
           yield movie, count        

if __name__ == '__main__':
    MoviePopularityRatings.run()
