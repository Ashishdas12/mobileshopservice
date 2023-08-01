from odoo import models, fields, api

class SalesReport(models.TransientModel):
    _name = 'sales.report'

    start_date = fields.Date()
    end_date = fields.Date()


    def sales_excel_report(self):
        print('Excel Report')
        sales = self.env['sale.sale'].search_read(
            [('pdate', '>=', self.start_date), ('pdate', '<=', self.end_date)])
        val = {
            'sales': sales,
            'start_d': self.start_date,
            'end_d': self.end_date

        }
        return self.env.ref('mobileshop.sale_excel_report').report_action(self, data=val)


    def sales_pdf_report(self):
        print("hai")
        store1 = {
            'ids': self.ids,
            'model': self._name,
            'form': {'start_d': self.start_date,
                     'end_d': self.end_date,
                     }, }
        return self.env.ref('mobileshop.ser_report').report_action(self, data=store1)


class service_abs(models.AbstractModel):
    _name = 'report.mobileshop.abs_rep'

    @api.model
    def _get_report_values(self, docids, data=None):
        start = data['form']['start_d']
        end = data['form']['end_d']
        print("------------------")

        filter = "sale_sale.pdate::date>='" + str(start) + "' and sale_sale.pdate::date<='" + str(
            end) + "'"
        qry = """select cname,phone,pdate,price from sale_sale where """ + str(filter) + """"""
        print(qry)

        docss = []
        self.env.cr.execute(qry)
        for d in self.env.cr.dictfetchall():
            docss.append({
                'name': d['cname'],
                'contact': d['phone'],
                'date': d['pdate'],
                'price': d['price'],
            })
        return {
            'res_id': 1,
            'res_model': 'reach.reach',
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'start_date': start,
            'end_date': end,
            'data': docss,
        }
