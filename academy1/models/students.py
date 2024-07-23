from odoo import models, fields

class Student(models.Model):
    _name = 'academy1.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    teacher_id = fields.Many2one('academy1.teacher', string='Teacher')