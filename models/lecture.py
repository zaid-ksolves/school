from odoo import api, fields, models

class Lecture(models.Model):
    _name = 'school.lecture'
    _description = 'Lecture'

    name = fields.Char(string='Name', required=True)
    hour = fields.Char(string='Hour')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
