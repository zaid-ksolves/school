from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _description="Students records"

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    age = fields.Integer(string='Age')
    subjects = fields.Many2many('school.lecture', string='Subjects')
    school_id = fields.Many2one('school.school', string='School')