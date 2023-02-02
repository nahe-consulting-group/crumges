# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerAttachmentTypeExpiration(http.Controller):
#     @http.route('/partner_attachment_type_expiration/partner_attachment_type_expiration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_attachment_type_expiration/partner_attachment_type_expiration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_attachment_type_expiration.listing', {
#             'root': '/partner_attachment_type_expiration/partner_attachment_type_expiration',
#             'objects': http.request.env['partner_attachment_type_expiration.partner_attachment_type_expiration'].search([]),
#         })

#     @http.route('/partner_attachment_type_expiration/partner_attachment_type_expiration/objects/<model("partner_attachment_type_expiration.partner_attachment_type_expiration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_attachment_type_expiration.object', {
#             'object': obj
#         })
