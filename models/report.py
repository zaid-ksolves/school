from odoo import models, fields, api

class Report(models.Model):
    _name = 'school.report'
    _description = 'Student Reports'

    name = fields.Char(string='Name', required=True)
    students = fields.One2many('school.student', 'school_id', string='Students')
    rollNo = fields.Char(string='Roll Number')

    @api.onchange('students')
    def onchange_students(self):
        self.rollNo= self.students.rollNo
        print("Triggered")