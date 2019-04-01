import tornado.web
import tornado.httpserver
import random
from methods import fake_database
import copy
import json


class RandomSelectHandler(tornado.web.RequestHandler):
    participant_set_copy = set()
    reward_record = {}

    def initialize(self, participant_set=fake_database.participant_set):
        self.participant_set_copy = copy.deepcopy(participant_set)

    def get(self):
        self.participant_set_copy.clear()
        self.participant_set_copy = copy.deepcopy(fake_database.participant_set)
        self.reward_record.clear()
        self.render('random_select.html', table="")

    def post(self):
        if self.get_argument("message") == "select":
            count = eval(self.get_argument("count", None))
            prize_type = self.get_argument("prize_type", None)
            to_be_selected = self.participant_set_copy.difference(set(self.reward_record.keys()))
            print(self.participant_set_copy)
            print(self.reward_record.keys())
            print(count, to_be_selected, len(to_be_selected))
            if (type(count) is int) and (count <= len(to_be_selected)):
                reward_set = random.sample(to_be_selected, count)
                for i in reward_set:
                    self.reward_record[i] = prize_type
                new_reward_record = []
                for i in self.reward_record.keys():
                    temp = list(i)
                    temp.append(self.reward_record[i])
                    new_reward_record.append(temp)
                print(new_reward_record)
                data = {'rewardRecord': new_reward_record,
                        'newReward': list(reward_set)}
                self.write(data)
            else:
                self.write(json.dumps(-1))
        elif self.get_argument("message") == "refresh":
            print("refresh")
            self.participant_set_copy.clear()
            self.participant_set_copy = copy.deepcopy(fake_database.participant_set)
            self.reward_record.clear()
            print(self.participant_set_copy)
            print(self.reward_record)
