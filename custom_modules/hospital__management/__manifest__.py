# -*- coding: utf-8 -*-
{
    'name': "Hospital_Management",

    'summary': "Managing  activities of doctors  and patient ",

    'description': """
Managing  activities of doctors  and patient
    """,

    'author': "Health",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_appointment_view.xml',
        'views/hospital_doctor_view.xml',
        'views/hospital_patient_view.xml',
        'data/sequence_appointment.xml',
        'report/patient_report_template.xml',
        'report/report_action.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

