# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class trabajadores_plugin_model(models.Model):
    _name = 'laboratorio_dental.trabajadores_model'
    _inherit='laboratorio_dental.trabajadores_model'
    _description = 'laboratorio_plugin'


    encargado=fields.Many2one("laboratorio_dental.trabajadores_model","Encargado")


    @api.constrains("encargado")
    def noPuedeSerEncargado(self):
        self.ensure_one()
        for i in self.encargado:
            if i.encargado==self.encargado:
                raise ValidationError("El encargado no puede ser uno mismo")

   


