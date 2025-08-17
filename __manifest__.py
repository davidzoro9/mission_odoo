{
    'name': "Personnel Mission GPT",
    'version': '1.0',
    'depends': ['base', 'hr', 'hr_attendance', 'hr_holidays', 'hr_contract',
    'hr_expense', 'fleet', 'contacts'],
    'author': "ZOROM",
    'category': 'hr',
    'description': """
    Gestion des missions
    """,
    
    'data': [
         'views/mission_action.xml',
         'views/mission_expense_views.xml',
         'views/mission_transport_views.xml',
         'data/cron_mission.xml',
         'views/mission_menus.xml',
         'views/mission_menus.xml',
         'views/mission_team_views.xml',
         'views/mission_views.xml',
         'views/templates.xml',
         'views/mission_validation_views.xml',


           'data/mission_tracking_sequence.xml',
    'views/mission_tracking_views.xml',
        # 'report/paperformat.xml',
    # 'report/report.xml',
    # 'report/report_mission_order.xml',
        #   'report/report_mission.xml',
        'views/parametrage_views.xml',
        # 'views/report_mission_order.xml',
        # 'views/report_mission_order_document.xml',
        
         'data/mission_sequence.xml',
        #'views/fleet_views.xml',
         'security/ir.model.access.csv',
    #    'static/description/icon.png',
        
          
         
    ],
   
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
   
    
}