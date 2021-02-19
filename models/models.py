# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class laboratorio_dental_plugin(models.Model):
#     _name = 'laboratorio_dental_plugin.laboratorio_dental_plugin'
#     _description = 'laboratorio_dental_plugin.laboratorio_dental_plugin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
