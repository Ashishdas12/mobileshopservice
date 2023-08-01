from odoo import models
class service_excel(models.TransientModel):
    _name = 'report.mobileshop.sale_excel_xlsx'
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self,workbook,data,mod):
        sheet = workbook.add_worksheet("Sales Details")
        bold = workbook.add_format({'bold':True})
        row = 3
        col = 3
        sheet.merge_range('C2:D2', data['start_d'])
        sheet.merge_range('C3:D3', data['end_d'])

        sheet.write(row,col,'Customer Name',bold)
        sheet.write(row, col + 1, 'Customer Number', bold)
        sheet.write(row, col + 2, 'Purchase report', bold)
        sheet.write(row, col + 3, 'Amount', bold)

        for x in data['sales']:
            row +=1
            sheet.write(row,col,x['cname'])
            sheet.write(row,col + 1,x['phone'])
            sheet.write(row,col + 2,x['pdate'])
            sheet.write(row,col + 3,x['price'])







