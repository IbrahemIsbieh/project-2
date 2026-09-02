from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Student(models.Model):
    _name = 'student.student'

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Student Name', required=True)
    phone = fields.Char(string='Student Phone',size=10)
    date_of_birth = fields.Date(string='Student Date', required=True)
    age=fields.Integer(string='Student Age',compute='_compute_age_')
    address = fields.Text(string='Student Address')
    active = fields.Boolean(string="Active", default=True)
    type=fields.Selection([('male','Male'),('female','Female')],default='male')
    enrollment_ids=fields.One2many('school.enrollment', "student_id")

    @api.constrains("age")
    def _check_age(self):
        for rec in self:
            if rec.age and (rec.age < 6 or rec.age > 12):
                raise ValidationError("Student Age must be between 6 and 12")

    @api.depends('date_of_birth')
    def _compute_age_(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = (today.year - rec.date_of_birth.year)
            else:
                rec.age = 0