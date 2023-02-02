# -*- coding: utf-8 -*-
{
    'name': "l10n_ar_field_partner_type_government",

    'summary': """
        cambiar algunas variables de res.partner""",

    'description': """
        --Cambiar la etiqueta "Individual" por "Persona Humana"
--Cambiar la etiqueta "Compañia" por "Persona Juridica"
--Agregar un campo mas de selección que se llame "Tipo de persona Juridica", 
y que sea invisible condicional solo si el tipo de company es "Persona Juridica", 
y que tenga dos valores: "Sociedades Simples", "Otras Sociedades"
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
