import typing
from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError
from datetime import date

class Student(models.Model):
    _name = 'student.student'

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Information'

    name = fields.Char(string='Student Name', required=True)
    phone = fields.Char(string='Student Phone',size=10)
    date_of_birth = fields.Date(string='Student Date', required=True)
    age=fields.Integer(string='Student Age',compute='_compute_age_')
    address = fields.Text(string='Student Address')
    active = fields.Boolean(string="Active", default=True)
    type=fields.Selection([('male','Male'),('female','Female')],default='male')
    enrollment_ids=fields.One2many('school.enrollment', "student_id")
    teacher_id=fields.Many2one('res.users',string='Teacher')
    parent_id = fields.Many2one('res.users', string='Parent')
    @api.constrains("age")
    def _check_age(self):
        for rec in self:
            if rec.age and (rec.age < 6 or rec.age > 15):
                raise ValidationError("Student Age must be between 6 and 15")

    @api.depends('date_of_birth')
    def _compute_age_(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = (today.year - rec.date_of_birth.year)
            else:
                rec.age = 0

    @api.constrains('phone')
    def _check_phone_number(self):
        for record in self:
            if record.phone:
                if not record.phone.isdigit():
                    raise ValidationError("Phone number must contain numbers only.")
                if not record.phone.startswith('0'):
                    raise ValidationError("Phone number must start with 0.")

    def unlink(self):
        if not self.env.user.has_group('school_app.group_manage'):
            raise UserError("You are not allowed to unlink this School Student.")
        return super(SchoolStudent, self).unlink()
