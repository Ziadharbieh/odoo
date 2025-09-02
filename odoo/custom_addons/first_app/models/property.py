from odoo import models,fields

class Property(models.Model):
    _name = "property"
    name = fields.Char()
    description = fields.Text()
