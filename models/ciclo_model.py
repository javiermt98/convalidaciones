 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class ciclo_model(models.Model):
    _name = 'convalidaciones.ciclo_model'
    _description = 'convalidaciones.ciclo_model'
    _sql_constraints =[("ciclos_name_unique","UNIQUE (name)","Ya existe un ciclo con ese nombre"),] 

    name = fields.Char(string="Ciclo", required="True", index="True", help="Añade el nombre del ciclo")
    descripcion = fields.Html(string="Descrpición del Ciclo", help="Pequeña introducción a lo que será el ciclo")
    modulos = fields.One2many("convalidaciones.modulo_model", "ciclo", string="Módulos")
