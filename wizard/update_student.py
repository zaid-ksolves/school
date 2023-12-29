from odoo import models, fields, api
from datetime import datetime


class UpdateStudentWizard(models.TransientModel):
    _name = 'update.student.wizard'
    _description = 'Update Student Wizard'

    name = fields.Char(string='Name', required=True)
    rollNo = fields.Char(string='Roll Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    age = fields.Integer(string='Age', compute='_compute_age')
    date_of_birth = fields.Date(string='DOB')
    subjects = fields.Many2many('school.class', string='Subjects')
    school_id = fields.Many2one('school.school', string='School')
    english = fields.Integer(string='English')
    hindi = fields.Integer(string='Hindi')
    physics = fields.Integer(string='Physics')
    maths = fields.Integer(string='Maths')
    chemistry = fields.Integer(string='Chemistry')
    total_marks = fields.Integer(string='Total Marks', compute='_compute_total_marks', store=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = datetime.now().date()
        for record in self:
            if record.date_of_birth:
                dob = fields.Date.from_string(record.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age
            else:
                record.age = 0

    def action_update_students(self):
        active_ids = self.env.context.get('active_ids')
        students = self.env['school.student'].browse(active_ids)
        # student=self.env['school.student']
        for student in students:
            student.write({
                'name': self.name,
                'rollNo': self.rollNo,
                'age': self.age,
                'date_of_birth': self.date_of_birth,
                'gender': self.gender,
                'english': self.english,
                'hindi': self.hindi,
                'maths': self.maths,
                'physics': self.physics,
                'chemistry': self.chemistry,
            })

    def default_get(self, fields_list):
        res = super(UpdateStudentWizard, self).default_get(fields_list)
        active_ids = self.env.context.get('active_ids')
        students = self.env['school.student'].browse(active_ids)

        for student in students:
            res.update({
                'name': student.name,
                'rollNo': student.rollNo,
                'age': student.age,
                'date_of_birth': student.date_of_birth,
                'gender': student.gender,
                'english': student.english,
                'hindi': student.hindi,
                'maths': student.maths,
                'physics': student.physics,
                'chemistry': student.chemistry,
            })
        return res
