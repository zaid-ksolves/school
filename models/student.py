from odoo import api, fields, models,_
from datetime import datetime
from odoo.exceptions import ValidationError
class SchoolStudent(models.Model):
    _name = "school.student"
    _description="Students records"

    name = fields.Char(string='Name', required=True)
    rollNo = fields.Char(string='Roll Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    age = fields.Integer(string='Age', compute='_compute_age')
    date_of_birth = fields.Date(string='DOB')
    school_id = fields.Many2one('school.school', string='School')
    class_line = fields.One2many('school.student_record','student_id',string="Class")

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

    @api.onchange('english', 'hindi', 'physics', 'maths', 'chemistry')
    def onchange_marks(self):
        self._compute_total_marks()

    # @api.constrains('name')
    # def check_name(self):
    #     for record in self:
    #         student = self.env['school.student'].search([('name','=',record.name),('id','!=',record.id)],order)
    #         if student:
    #             raise ValidationError(_('Student Already exists.'))

    _sql_constraints = [
        ('unique_tag_name','unique(name)','Name must be unique')
    ]


