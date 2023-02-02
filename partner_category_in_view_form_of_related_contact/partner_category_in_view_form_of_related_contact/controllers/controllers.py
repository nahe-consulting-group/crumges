# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerCategoryInViewFormOfRelatedContact(http.Controller):
#     @http.route('/partner_category_in_view_form_of_related_contact/partner_category_in_view_form_of_related_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_category_in_view_form_of_related_contact/partner_category_in_view_form_of_related_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_category_in_view_form_of_related_contact.listing', {
#             'root': '/partner_category_in_view_form_of_related_contact/partner_category_in_view_form_of_related_contact',
#             'objects': http.request.env['partner_category_in_view_form_of_related_contact.partner_category_in_view_form_of_related_contact'].search([]),
#         })

#     @http.route('/partner_category_in_view_form_of_related_contact/partner_category_in_view_form_of_related_contact/objects/<model("partner_category_in_view_form_of_related_contact.partner_category_in_view_form_of_related_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_category_in_view_form_of_related_contact.object', {
#             'object': obj
#         })
