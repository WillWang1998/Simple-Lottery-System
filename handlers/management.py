import tornado.web
import tornado.httpserver
import json
from methods import fake_database


class ManagementHandler(tornado.web.RequestHandler):
    def get(self):
        table = json.dumps(list(fake_database.participant_set))
        print(table)
        self.render('management.html', table=table)

    def post(self):
        com = eval(self.get_argument("command"))
        if com == 1:
            phone = self.get_argument("phone")
            name = self.get_argument("name")
            print(phone, name)
            val = fake_database.update(phone, name)
            self.write(json.dumps(val))
        else:
            phone = self.get_argument("phone")
            val = fake_database.delete(phone)
            self.write(json.dumps(val))
