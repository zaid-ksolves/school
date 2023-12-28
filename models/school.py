from odoo import models, fields, api

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string='Name', required=True)
    students = fields.One2many('school.student', 'school_id', string='Students')
