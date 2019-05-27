
{
    'name': 'customPOS',
    'summary': '',
    'version': '1.0',

    'description': """

    """,

    # 'author': '',
    # 'maintainer': '',
    # 'contributors': [''],

    # 'website': '',

    'license': 'AGPL-3',
    'category': '',

    'depends': [
        'base', 'point_of_sale',
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'views/templates.xml',

    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    'static/src/css/custom.css',
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
