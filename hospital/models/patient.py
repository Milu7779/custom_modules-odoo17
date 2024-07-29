from odoo import models,fields

class Patient(models.Model):
     _name = 'hospital.patient'
     _description = 'Patient'

     name = fields.Char(string='Name')
     age = fields.Integer(string='Age')
     gender = fields.Selection([('male' , 'Male') , ('female' , 'Female')], string='Gender')
     phone_no = fields.Char(string='Phone Number')
     appointment_id = fields.One2many('hospital.appointment', 'patient_id', string='Appointment')