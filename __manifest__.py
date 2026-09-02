{
    'name': 'School Management System',
    'version': '19.0.1.0.0',
    'summary': 'School Management System',
    'author': 'ibrahim',
    'category': 'Services',
    'depends': ['base','web'],

    'data': [  'security/ir.model.access.csv',
               'views/base_menu.xml',
               'views/student_view.xml',
               'views/course_view.xml',
               'views/enrollment_view.xml',

    ],
'assets': {
        'web.assets_backend': [
            'school_app/static/src/index.css',
        ],
    },
    'installable': True,
    'application': True,
}