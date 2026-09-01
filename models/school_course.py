from odoo import models, fields
class school_course(models.Model):
    _name = 'school.course'
    _description = 'School Information'

    name = fields.Char('Course Name', required=True)
    description = fields.Text('Course Description')
    active = fields.Boolean()
    enrollment_ids=fields.One2many('school.enrollment', "course_id")


