import re
import operator
import geoip2.database
import sys

reader = geoip2.database.Reader('./db/GeoLite2-Country.mmdb')
IP_RE = re.compile(r"^\d+\.\d+\.\d+")


def simple_run():
    countries = {}
    with open(sys.argv[1]) as file:
        for line in file:
            ip = '%s.0' % IP_RE.search(line).group(0)
            country = reader.country(ip).country.name
            if country not in countries:
                countries[country] = 1
            else:
                countries[country] += 1
    sorted_x = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x[:1])


if __name__ == '__main__':
    simple_run()
