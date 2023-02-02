# -*- coding: utf-8 -*-
{
    'name': "partner_company_name_fantasy",

    'summary': """
        cambio a la vista de ref en el form de res.partner""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
