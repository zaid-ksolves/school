from odoo import api, fields, models

class schoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    teachers = fields.Many2many('school.teacher','school_class_teacher_1_rel','class_id','teacher_id' ,string='Teachers')
