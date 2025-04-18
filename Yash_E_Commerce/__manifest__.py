# -*- coding: utf-8 -*-
{
    'name': 'Simple E-Commerce',
    'summary': 'Manage simple products for E-Commerce (Backend only)',
    'description': 'This module adds a basic product model for an e-commerce backend without website features.',
    'author': 'YashwanthReddyL',
    'website': 'http://yourwebsite.com',
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
}

