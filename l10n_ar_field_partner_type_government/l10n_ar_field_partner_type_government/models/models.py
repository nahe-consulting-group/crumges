# -*- coding: utf-8 -*-

from odoo import models, fields, api


class l10n_ar_field_partner_type_government(models.Model):
	_inherit = 'res.partner'

	company_type = fields.Selection(string='Tipo de Personeria',
        selection=[('person', 'Persona Humana'), ('company', 'Persona Jurídica')],
        compute='_compute_company_type', inverse='_write_company_type')
	company_type_subtype = fields.Selection(string='Tipo de Personeria Jurídica',
        selection=[('simple', 'Sociedades Simples'), ('other', 'Otras Sociedades')])
