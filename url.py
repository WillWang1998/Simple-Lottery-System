import sys
from importlib import reload
from handlers import index
from handlers import randomselect
from handlers import management
from methods import fake_database
reload(sys)

url = [
    (r"/", index.IndexHandler),
    (r"/random_select", randomselect.RandomSelectHandler,
     dict(participant_set=fake_database.participant_set)),
    (r"/management", management.ManagementHandler)
]

