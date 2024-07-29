from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference No", default='New')
    date = fields.Datetime(string='Date')
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor Name')
    patient_id = fields.Many2one('hospital.patient',string='Patient Name')
    gender = fields.Selection([('male','Male'),('female','Female')],string='patient Gender',related='patient_id.gender')

    @api.model_create_multi
    def create(self, vals_list):
            print('current record to be saved', vals_list)
            for vals in vals_list:
                if not vals.get('reference') or vals['reference'] == 'New':
                    vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
            return super().create(vals_list)

