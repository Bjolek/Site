from DBManager import DBmanager

db_manager = DBmanager("Site.db")
db_manager.create_table()
#db_manager.add_quize(1,
       #              "Квіз про Україну",
        #        "деякі значення"
        #        )
#db_manager.add_question(1,1,"Коли відмінили кріпосне право")
db_manager.get_options(1,1,"1840")
db_manager.get_options(1,2,"1846")
db_manager.get_options(1,3,"1848")

