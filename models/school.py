from odoo import models, fields, api

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string='Name', required=True)
    students_line = fields.One2many('school.student', 'school_id', string='Students')
    rollNo = fields.Char(string='Roll Number')

    @api.onchange('students')
    def onchange_students(self):
        self.rollNo= self.students.rollNo
        print("Triggered")