# -*- coding: utf-8 -*-
from odoo import models, fields

class EcommerceProduct(models.Model):
    _name = 'ecommerce.product'
    _description = 'E-Commerce Product'

    name = fields.Char(string='Product Name', required=True)
    price = fields.Float(string='Price', required=True)
    description = fields.Text(string='Description')
    available = fields.Boolean(string='Available', default=True)

