import csv
import os


class CSVReader:

    @staticmethod
    def read_csv(file_name):

        data = []

        file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "testdata",
            file_name
        )

        with open(file_path, newline="", encoding="utf-8") as csvfile:

            reader = csv.reader(csvfile)

            next(reader)  # Skip header

            for row in reader:

                data.append(tuple(row))

        return data