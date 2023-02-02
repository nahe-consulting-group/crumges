# -*- coding: utf-8 -*-

from odoo import models, fields, api

class naherelatedattachment(models.Model):
	_inherit = 'res.partner'

	attachment_ids_r = fields.Many2many('ir.attachment', string='Adjuntos',)

	@api.onchange('message_attachment_count')
	def _onchange_message_attachment_count(self):
		attachments = self.env['ir.attachment'].search([('res_model', '=', 'res.partner'), ('res_id', '=', self.id)])
		self.attachment_ids_r = [(6, 0, attachments.ids)]