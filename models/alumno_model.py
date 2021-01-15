# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError


class alumno_model(models.Model):
    _name = 'convalidaciones.alumno_model'
    _description = 'convalidaciones.alumno_model'

    name = fields.Char(string="Nombre", required=True, index=True)
    password = fields.Char(string="Contraseña", required=False, default="123", size=11)
    foto = fields.Binary()
    edad = fields.Integer(string="Edad", required=True, index=True, )
    localidad = fields.Char(string="Localidad", size=50, required=True, index=True)
    provincia = fields.Char(string="Provincia", size=50, required=True, index=True)
    email = fields.Char(string="Email", size=100, required=True, )
    conv_alu = fields.One2many("convalidaciones.conv_model", "alumno_id", "Módulos convalidados")
    profesores = fields.Many2many("convalidaciones.profesor_model", string="Profesores")

    def generaPass(self):
        longitud = 10
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        self.password = p
        return True
    
    @api.constrains("edad")
    def _check_edad(self):
        if self.edad<0:
            raise ValidationError("No puede haber una edad negativa")
        return True
