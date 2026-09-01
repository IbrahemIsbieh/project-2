from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Student Name', required=True)
    phone = fields.Integer(string='Student Phone', required=True)
    date = fields.Date(string='Student Date', required=True)
    address = fields.Text(string='Student Address')
    active = fields.Boolean()
    enrollment_ids=fields.One2many('school.enrollment', "student_id")
