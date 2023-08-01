# -*- coding: utf-8 -*-
# from odoo import http


# class Mobileshop(http.Controller):
#     @http.route('/mobileshop/mobileshop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mobileshop/mobileshop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mobileshop.listing', {
#             'root': '/mobileshop/mobileshop',
#             'objects': http.request.env['mobileshop.mobileshop'].search([]),
#         })

#     @http.route('/mobileshop/mobileshop/objects/<model("mobileshop.mobileshop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mobileshop.object', {
#             'object': obj
#         })
