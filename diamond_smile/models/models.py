
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class diamond_smile(models.Model):
     _name = 'diamond_smile.diamond_smile'
     _description = 'diamond_smile.diamond_smile'

     doctor_id = fields.Many2one('hr.employee', required=True)
     service = fields.Selection([
         ('consultation', 'consultation'),
         ('extraction', 'extraction'),
         ('root canel', 'root canel'),
         ('cleaning', 'cleaning'),
         ('follow up', 'follow up'),
         ('filling', 'filling'),
         ('visting', 'visting'),
         ('crown', 'crown'),
         ('x-ray', 'x-ray'),
         ('adjustment', 'adjustment'),
         ('braces installation', 'braces installation'),

     ])
     duration = fields.Char(compute="_value_pc", store=True)
     app_date = fields.Date()
     patient_first_name = fields.Char()
     patient_last_name = fields.Char()
     Gender = fields.Selection([
         ('male', 'male'),
         ('female', 'female'),
         ('other', 'other'),
     ])
     phone = fields.Integer()
     email = fields.Char()


     @api.onchange('service')
     def _value_pc(self):
         for record in self:
             if record.service == "consultation":
                 record.duration = "30min"
             elif record.service == "extraction":
                 record.duration = "45min"
             elif record.service == "root canel":
                 record.duration = "40min"
             elif record.service == "cleaning":
                 record.duration = "30min"
             elif record.service == "follow up":
                 record.duration = "30min"
             elif record.service == "filling":
                 record.duration = "30min"
             elif record.service == "visting":
                 record.duration = "30min"
             elif record.service == "crown":
                 record.duration = "2hrs"
             elif record.service == "x-ray":
                 record.duration = "30min"
             elif record == "adjustment":
                 record.duration = "30min"
             elif record.service == "brace installation":
                 record.duration = "1h30min"
