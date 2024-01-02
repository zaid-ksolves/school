from odoo.exceptions import ValidationError
from odoo import models, fields, api
class SchoolStudent(models.Model):
    _name = "school.student_record"
    _description="Students subjects records"

    class_id = fields.Many2one('school.class',String="Class")
    english = fields.Integer(string='English')
    hindi = fields.Integer(string='Hindi')
    physics = fields.Integer(string='Physics')
    maths = fields.Integer(string='Maths')
    chemistry = fields.Integer(string='Chemistry')
    total_marks = fields.Integer(string='Total Marks', compute='_compute_total_marks', store=True)
    student_id = fields.Many2one('school.student', string='Student')

    @api.depends('english', 'hindi', 'physics', 'maths', 'chemistry')
    def _compute_total_marks(self):
        for record in self:
            total = 0
            subjects = ['english', 'hindi', 'physics', 'maths', 'chemistry']
            for subject in subjects:
                marks = getattr(record, subject, '0') or '0'
                total += int(marks)
            record.total_marks = total

    @api.onchange('english', 'hindi', 'physics', 'maths', 'chemistry')
    def onchange_marks(self):
        self._compute_total_marks()