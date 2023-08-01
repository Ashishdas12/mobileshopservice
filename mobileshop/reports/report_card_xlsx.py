from odoo import models


class reportxlsx(models.AbstractModel):
    _name = 'report.mobileshop.sales_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # print("lines", lines)
        format1 = workbook.add_format({'font_size': 10, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('sale_Card')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.cname, format2)
        sheet.write(3, 2, 'Address', format1)
        sheet.write(3, 3, lines.add, format2)
        sheet.write(4, 2, 'Phone', format1)
        sheet.write(4, 3, lines.phone, format2)
        sheet.write(5, 2, 'EMEI', format1)
        sheet.write(5, 3, lines.imi, format2)
        sheet.write(6, 2, 'QUantity', format1)
        sheet.write(6, 3, lines.qty, format2)
        sheet.write(7, 2, 'Price', format1)
        sheet.write(7, 3, lines.price, format2)
        sheet.write(8, 2, 'warranty', format1)
        sheet.write(8, 3, lines.war, format2)



# mobiles excel cards

class mobxlsx(models.AbstractModel):
    _name = 'report.mobileshop.mobiles_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # print("lines", lines)
        format1 = workbook.add_format({'font_size': 10, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('mobiles_Card')
        sheet.write(2, 2, 'ID', format1)
        sheet.write(2, 3, lines.mob_seq, format2)
        sheet.write(3, 2, 'Name', format1)
        sheet.write(3, 3, lines.name, format2)
        sheet.write(4, 2, 'Model', format1)
        sheet.write(4, 3, lines.model, format2)
        sheet.write(5, 2, 'Qunty', format1)
        sheet.write(5, 3, lines.qty, format2)
        sheet.write(6, 2, 'Stock Date', format1)
        sheet.write(6, 3, lines.sd, format2)
        sheet.write(7, 2, 'Company Price', format1)
        sheet.write(7, 3, lines.cp, format2)
        sheet.write(8, 2, 'Customer Price', format1)
        sheet.write(8, 3, lines.csp, format2)

