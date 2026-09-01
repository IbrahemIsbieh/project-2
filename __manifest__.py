{
    'name': 'School Management System',
    'version': '19.0.1.0.0',
    'summary': 'School Management System',
    'author': 'ibrahim',
    'category': 'Services',
    'depends': ['base'],
    'data': [  'security/ir.model.access.csv',
               'views/base_menu.xml',
               'views/student_view.xml',
               'views/course_view.xml',
               'views/enrollment_view.xml',

    ],
    'installable': True,
    'application': True,
}