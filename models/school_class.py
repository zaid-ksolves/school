from odoo import api, fields, models

class schoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    teachers_ids = fields.Many2many('school.teacher','school_class_teacher_1_rel','class_id','teacher_id' ,string='Teachers')
    # subject =  fields.Char(string='Subject')
    # percentage = fields.Char(string='Percentage')
    # english = fields.Integer(string='English')
    # hindi = fields.Integer(string='Hindi')
    # physics = fields.Integer(string='Physics')
    # maths = fields.Integer(string='Maths')
    # chemistry = fields.Integer(string='Chemistry')
    # total_marks = fields.Integer(string='Total Marks', compute='_compute_total_marks', store=True)
    # student_id = fields.Many2one('school.student', string="Student")

    # @api.depends('date_of_birth')
    # def _compute_age(self):
    #     today = datetime.now().date()
    #     for record in self:
    #         if record.date_of_birth:
    #             dob = fields.Date.from_string(record.date_of_birth)
    #             age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    #             record.age = age
    #         else:
    #             record.age = 0

    # @api.depends('english', 'hindi', 'physics', 'maths', 'chemistry')
    # def _compute_total_marks(self):
    #     for record in self:
    #         total = 0
    #         subjects = ['english', 'hindi', 'physics', 'maths', 'chemistry']
    #         for subject in subjects:
    #             marks = getattr(record, subject, '0') or '0'
    #             total += int(marks)
    #         record.total_marks = total
