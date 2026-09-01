from odoo import models, fields

class school_enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'School Enrollment'


    enrollment_date = fields.Date(string='Enrollment Date',default='fields.Date.today()')
    grade = fields.Float(string='Grade')
    active = fields.Boolean()
    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course')