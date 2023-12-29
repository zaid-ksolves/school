from odoo import models, fields, api
from datetime import datetime

class CreateStudentWizard(models.TransientModel):
    _name = 'notice.wizard'
    _description = 'Notice Wizard'

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

    @api.depends('english', 'hindi', 'physics', 'maths', 'chemistry')
    def _compute_total_marks(self):
        for record in self:
            total = 0
            subjects = ['english', 'hindi', 'physics', 'maths', 'chemistry']
            for subject in subjects:
                marks = getattr(record, subject, '0') or '0'
                total += int(marks)
            record.total_marks = total


    def action_enroll_students(self):
        student = self.env['school.student']
        new_student=student.create({
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
        return new_student

    def default_get(self,fields_list):
        print('Helloo.....')
        return super(CreateStudentWizard, self).default_get(fields_list)