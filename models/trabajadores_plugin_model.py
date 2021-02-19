# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class trabajadores_plugin_model(models.Model):
    _name = 'laboratorio_dental.trabajadores_model'
    _inherit='laboratorio_dental.trabajadores_model'
    _description = 'laboratorio_plugin'


    edad=fields.Integer(string="Edad",required=True)

    @api.constrains("edad")
    def esMayor(self):
        if self.edad<16:
            raise ValidationError("Debe tener al menos 16 años")


