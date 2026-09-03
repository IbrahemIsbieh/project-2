from odoo import models, fields,api
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    student_id = fields.Many2one('school.student', string='Student')

    @api.onchange('student_id')
    def _onchange_student_id(self):
        for record in self:
            if record.student_id and record.student_id.parent_id:
                # parent_id عبارة عن res.users
                # نصل إلى partner_id المباشر التابع لهذا المستخدم
                record.partner_id = record.student_id.parent_id.partner_id