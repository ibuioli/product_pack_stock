{
    'name': 'Product Pack',
    'version': '12.0.1.0.0',
    'summary': 'Manage Products as Pack',
    'description': 'Manage Products as Pack',
    'category': 'Sales',
    'author': 'Cybrosys Techno Solutions, Moldeo Interactive',
    'company': 'Cybrosys Techno Solutions, Moldeo Interactive',
    'maintainer': 'Cybrosys Techno Solutions, Moldeo Interactive',
    'website': 'https://www.moldeointeractive.com.ar',
    'depends': ['base', 'sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_form_view.xml',
        'wizard/select_product_pack_view.xml',
        'views/sale_order_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,
}
