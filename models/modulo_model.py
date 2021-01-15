 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class modulo_model(models.Model):
    _name = 'convalidaciones.modulo_model'
    _description = 'convalidaciones.modulo_model'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción",required=False)
    horas = fields.Integer(string="Horas del módulo",required=False,default=8)
    ciclo = fields.Many2one("convalidaciones.ciclo_model", string="Ciclo")
