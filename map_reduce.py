import re
import geoip2.database
from mrjob.job import MRJob
from mrjob.step import MRStep

IP_RE = re.compile(r"^\d+\.\d+\.\d+")
limit = 5


class MRMostFrequentCountries(MRJob):

    def configure_args(self):
        super(MRMostFrequentCountries, self).configure_args()
        self.add_file_arg('--database')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_countries,
                   combiner=self.combiner_count_countries,
                   reducer=self.reducer_count_countries),
            MRStep(reducer=self.reducer_find_max_countries)
        ]

    def mapper_get_countries(self, _, line):
        reader = geoip2.database.Reader(self.options.database)
        ip = '%s.0' % IP_RE.search(line).group(0)
        country = reader.country(ip).country.name
        yield country, 1

    def combiner_count_countries(self, country, occurrence):
        yield (country, sum(occurrence))

    def reducer_count_countries(self, country, occurrence):
        yield None, (sum(occurrence), country)

    def reducer_find_max_countries(self, _, country_occurrence_pairs):
        yield max(country_occurrence_pairs)


if __name__ == '__main__':
    MRMostFrequentCountries.run()
