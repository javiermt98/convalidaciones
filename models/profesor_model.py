from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError


class profesor_model(models.Model):
    _name = 'convalidaciones.profesor_model'
    _description = 'convalidaciones.profesor_model'

    name = fields.Char(string="Nombre", required=True, index=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    foto = fields.Binary()
    DNI = fields.Char(string="DNI", required=True)
    numalu = fields.Integer(string="Número de alumnos", compute="_getNumalu", store=True)
    alumnos = fields.Many2many("convalidaciones.alumno_model", String="Alumnos")

    @api.constrains("DNI")
    def _comprobarDNI(self):
        if len(self.DNI)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.DNI[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.DNI[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")

    @api.depends("alumnos")
    def _getNumalu(self):
        self.numalu = len(self.alumnos)