import csv
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter


class ExcelReportGenerator:
    def __init__(self, csv_filepath, xlsx_filename):
        self.csv_filepath = csv_filepath
        self.xlsx_filename = xlsx_filename
        self.data = []

    def read_csv(self) -> None:
        try:
            with open(self.csv_filepath, 'r') as f:
                self.data = list(csv.reader(f))
        except FileNotFoundError:
            print("Csv File does not exist.")
        except Exception as e:
            print(f"Error! Message: {str(e)}")
            
        
    def build_workbook(self) -> None:
        self.wb = Workbook()
        self.ws = self.wb.active

        self.ws.append(self.data[0]) 

        for col_num in range(1, len(self.data[0]) + 1):
            self.ws.cell(row=1, column=col_num).font = Font(bold = True)

        for i in self.data[1:]:
            self.ws.append(i)

        for col_num in range(1, len(self.data[0]) + 1):
            max_length = max(len(str(row[col_num - 1])) for row in self.data)
            self.ws.column_dimensions[get_column_letter(col_num)].width = max_length + 2

    def save_xlsx(self) -> None:
        try:
            print(f"Report saved as: {self.xlsx_filename}")
        except Exception as ex:
            print(f"Error saving file: {str(ex)}")

    def add_chart(self):
        chart = BarChart()
        chart.title = "Quantity By Product"

        data = Reference(self.ws, min_col = 3, min_row = 1, max_row=len(self.data))
        categories = Reference(self.ws, min_col = 2, min_row = 2, max_row = len(self.data))


        chart.add_data(data, titles_from_data = True)
        chart.set_categories(categories)


        self.ws.add_chart(chart, "F2")
def main():

    report = ExcelReportGenerator('sales_data.csv', 'report')

    report.read_csv()
    report.build_workbook()
    report.add_chart()
    report.save_xlsx()

main()