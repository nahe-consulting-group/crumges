# -*- coding: utf-8 -*-
# from odoo import http


# class L10nArFieldPartnerTypeGovernment(http.Controller):
#     @http.route('/l10n_ar_field_partner_type_government/l10n_ar_field_partner_type_government', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ar_field_partner_type_government/l10n_ar_field_partner_type_government/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ar_field_partner_type_government.listing', {
#             'root': '/l10n_ar_field_partner_type_government/l10n_ar_field_partner_type_government',
#             'objects': http.request.env['l10n_ar_field_partner_type_government.l10n_ar_field_partner_type_government'].search([]),
#         })

#     @http.route('/l10n_ar_field_partner_type_government/l10n_ar_field_partner_type_government/objects/<model("l10n_ar_field_partner_type_government.l10n_ar_field_partner_type_government"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ar_field_partner_type_government.object', {
#             'object': obj
#         })
