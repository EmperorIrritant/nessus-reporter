import sys, os, re
from bs4 import BeautifulSoup
from glob import glob

class NessusReport:

    critical_color = "#d43f3a"
    high_color = "#ee9336"
    medium_color = "#fdc431"

    def __init__(self, report_file):
        self.report_file = report_file
        self._make_soup()

    def _make_soup(self):
        with self.report_file as nessus_report:
            self.soup = BeautifulSoup(nessus_report.read(), features="lxml")

class NessusReporter:

    def __init__(self, path):
        self.report_files_glob = path + os.sep + '*.html'
        self.report_files_list = glob(self.report_files_glob)
        self.reports = []
        self._add_reports()

    def _add_reports(self):
        for report in self.report_files_list:
            self.reports.append(NessusReport(report))


def main():
    file_path = sys.argv[1]
    reporter = NessusReporter(file_path)


if __name__ == "__main__":
    main()