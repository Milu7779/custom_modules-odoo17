from odoo import models, fields

class Teacher(models.Model):
    _name = 'academy1.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    department = fields.Char(string='Department')
