from odoo import models, fields
class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'School Course'

    name = fields.Char('Course Name', required=True)
    description = fields.Text('Course Description')
    active = fields.Boolean()
    enrollment_ids=fields.One2many('school.enrollment', "course_id")
    state=fields.Selection([
                                   ('draft','Draft'),
                                   ('scheduled','Scheduled'),
                                   ('start','In progress'),
                                   ('done','Completed'),
                                   ('cancel','Cancelled') ],default='draft')


    def action_schedule(self):
        for rec in self:
            rec.state="scheduled"


    def action_start(self):
         for rec in self:
             rec.state = "start"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"