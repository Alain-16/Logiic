# -*- coding: utf-8 -*-
# from odoo import http


# class DiamondSmile(http.Controller):
#     @http.route('/diamond_smile/diamond_smile', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diamond_smile/diamond_smile/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('diamond_smile.listing', {
#             'root': '/diamond_smile/diamond_smile',
#             'objects': http.request.env['diamond_smile.diamond_smile'].search([]),
#         })

#     @http.route('/diamond_smile/diamond_smile/objects/<model("diamond_smile.diamond_smile"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diamond_smile.object', {
#             'object': obj
#         })
