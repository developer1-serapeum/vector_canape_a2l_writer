import re
from openpyxl import Workbook
from openpyxl import load_workbook


"""
The goal of this script write to read parameters from excel sheet
"""

class SpreadSheetReader():

    def __init__(self):
        pass

    def readParameter(self, fileName, tabName, paremeterName):
        """
        Read a single parameter
        """
        wb = load_workbook(filename = fileName)
        sheet_ranges = wb[tabName]
        print(sheet_ranges['A2'].value)
        print(sheet_ranges['E2'].value)
        print(sheet_ranges['F2'].value)


    def findPattern(self):
        """
        [For debug only] Finds a desired pattern within a text file
        and writes it to an output file
        """
        file_in = 'compiler_in.txt'
        file_out = 'compiler_warning_ids.txt'
        pattern = re.compile(r"warning\s(#.+-.):")
        
        match_count = 0
        found_instances = []
        for i, line in enumerate(open(file_in)):
            for match in re.finditer(pattern, line):
                print ('Found on line %s: %s' % (i+1, match.group()) )
                found_instances.append(match.group(1))
                match_count += 1

        print("The pattern was found ({}) times".format(match_count))

        with open(file_out, 'w') as f:
            for line in found_instances:
                f.write("%s\n" % line)


    def print_rows(self):
        """
        [For debug only] It makes it easier to print all of your spreadsheet values by
        just calling print_rows().
        """
        workbook = Workbook()
        sheet = workbook.active
        for row in sheet.iter_rows(values_only=True):
            print(row)
