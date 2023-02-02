# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerCompanyNameFantasy(http.Controller):
#     @http.route('/partner_company_name_fantasy/partner_company_name_fantasy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_company_name_fantasy/partner_company_name_fantasy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_company_name_fantasy.listing', {
#             'root': '/partner_company_name_fantasy/partner_company_name_fantasy',
#             'objects': http.request.env['partner_company_name_fantasy.partner_company_name_fantasy'].search([]),
#         })

#     @http.route('/partner_company_name_fantasy/partner_company_name_fantasy/objects/<model("partner_company_name_fantasy.partner_company_name_fantasy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_company_name_fantasy.object', {
#             'object': obj
#         })
