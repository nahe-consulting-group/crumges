# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class partner_category_in_view_form_of_related_contact(models.Model):
#     _name = 'partner_category_in_view_form_of_related_contact.partner_category_in_view_form_of_related_contact'
#     _description = 'partner_category_in_view_form_of_related_contact.partner_category_in_view_form_of_related_contact'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
