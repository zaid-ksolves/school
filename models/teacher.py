from odoo import api, fields, models

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    classes = fields.Many2many('school.class','school_class_teacher_1_rel','teacher_id','class_id', string='Classes')