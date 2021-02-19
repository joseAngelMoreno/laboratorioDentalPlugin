# -*- coding: utf-8 -*-
# from odoo import http


# class LaboratorioDentalPlugin(http.Controller):
#     @http.route('/laboratorio_dental_plugin/laboratorio_dental_plugin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laboratorio_dental_plugin/laboratorio_dental_plugin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laboratorio_dental_plugin.listing', {
#             'root': '/laboratorio_dental_plugin/laboratorio_dental_plugin',
#             'objects': http.request.env['laboratorio_dental_plugin.laboratorio_dental_plugin'].search([]),
#         })

#     @http.route('/laboratorio_dental_plugin/laboratorio_dental_plugin/objects/<model("laboratorio_dental_plugin.laboratorio_dental_plugin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laboratorio_dental_plugin.object', {
#             'object': obj
#         })
