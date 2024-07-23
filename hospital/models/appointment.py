from odoo import models,fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    date = fields.Datetime(string='Date')
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor')
    patient_id = fields.Many2one('hospital.patient',string='Patient')
