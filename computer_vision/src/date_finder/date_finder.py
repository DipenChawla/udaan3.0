import datefinder
from dateparser.search import search_dates

#string_with_dates = "13/11/2019 sale fters, 2009-06-15T13:45:30"

class DateParser:
    def custom_date_parser_1(self, string_with_dates):
        fin_matches = []
        try:
            matches = datefinder.find_dates(string_with_dates)
            for match in matches:
                if (
                    not int(match.strftime("%Y")) < 2018
                    and not int(match.strftime("%Y")) > 2020
                ):
                    fin_matches.append(match)
            return fin_matches
        except:
            return []

    def custom_date_parser_2(self, string_with_dates):
        return [dt for _, dt in search_dates(string_with_dates)]

    def get_custom_date(self,string_with_dates):
        d1, d2 = (
            set(self.custom_date_parser_2(string_with_dates)),
            set(self.custom_date_parser_1(string_with_dates)),
        )
        print(d1, d2)
        intersection_date = d1.intersection(d2)
        if not intersection_date:
            return d1
        return intersection_date

# if __name__ == "__main__":
#     DateParser().get_custom_date(string_with_dates)
