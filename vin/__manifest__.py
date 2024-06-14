{
    "name": "Vin Search Module",
    "version": "1.0",
    "summary": "Module for managing vin search",
    "description": "This module allows users to managing vin search.",
    "author": "Wazizzz",
    "category": "Custom",
    "depends": ["base"],
    "data": [
        "views/vin_views.xml",
    ],
    'qweb': [
        'vin/static/src/xml/extend_vin_kanban.xml',
    ],
    "application": True,
    'assets': {
        'web.assets_backend': [
            'vin/static/src/js/extend_vin_kanban.js',
        ],
    },
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3"
}
