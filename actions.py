from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
from rasa_core_sdk import Action


weekday_dict = {0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}


class DisplayOff(Action):

    def name(self):
        return "action_display_off"

    def run(self, dispatcher, tracker, domain):
        """Return weekday using datetime"""

        duration = tracker.get_latest_entity_values("duration")

        time_list = list(duration)
        time_sum = sum(time_list)
        print(list(duration))
        print(type(time_list))
        print(time_sum)

        mydelta = datetime.timedelta(seconds=time_sum)
        mytime = datetime.datetime.min + mydelta
        h, m, s = mytime.hour, mytime.minute, mytime.second
        if h == 0 :
            if m == 0:
                dispatcher.utter_message("1분 보다 커야 합니다")
            else:
                dispatcher.utter_message("{}분 으로 설정합니다".format(m))
        else:
            if m == 0 :
                    dispatcher.utter_message("{}시간으로 설정합니다".format(h))
            else:
                dispatcher.utter_message("{}시간 {}분으로 설정합니다".format(h,m))
        return []


class DaySearch(Action):

    def name(self):
        return "action_day_search"

    def run(self, dispatcher, tracker, domain):
        """Return weekday using datetime"""

        date = next(tracker.get_latest_entity_values("time"), None)

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        week = datetime.datetime(year, month, day)
        weekday_idx = week.weekday()
        weekday = weekday_dict[weekday_idx]

        dispatcher.utter_message("{}년 {}월 {}일은 {} 입니다".format(year, month, day, weekday))

        return []


class DateSearch(Action):

    def name(self):
        return "action_date_search"

    def run(self, dispatcher, tracker, domain):
        """Return date using datetime"""
        # day_name =  next(tracker.get_latest_entity_values("day"), None)
        date = next(tracker.get_latest_entity_values("time"), None)

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])

        dispatcher.utter_message("{}년 {}월 {}일 입니다".format(year, month, day))

        return []


class SoundChange(Action):

    def name(self):
        return "action_sound_change"

    def run(self, dispatcher, tracker, domain):
        volume = next(tracker.get_latest_entity_values("number"), None)

        # volume = tracker.get_latest_integer_text_values()

        if int(volume) < 0:
            dispatcher.utter_message("시스템 볼륨은 0 보다 작을수 없습니다")
        elif int(volume) > 100:
            dispatcher.utter_message("시스템 볼륨은 100 보다 클수 없습니다")
        else:
            dispatcher.utter_message("시스템 볼륨을 {} 으로 설정합니다".format(volume))
        return []


class SoundUp(Action):

    def name(self):
        return "action_sound_up"

    def run(self, dispatcher, tracker, domain):
        volume = next(tracker.get_latest_entity_values("number"), None)

        # volume = tracker.get_latest_integer_text_values()

        if int(volume) < 0:
            dispatcher.utter_message("시스템 볼륨은 0 보다 작을수 없습니다")
        elif int(volume) > 100:
            dispatcher.utter_message("시스템 볼륨은 100 보다 클수 없습니다")
        else:
            dispatcher.utter_message("시스템 볼륨을 {} 으로 올립니다".format(volume))
        return []


class SoundDown(Action):

    def name(self):
        return "action_sound_down"

    def run(self, dispatcher, tracker, domain):
        volume = next(tracker.get_latest_entity_values("number"), None)
        volume = round(float(volume))
        # volume = tracker.get_latest_integer_text_values()

        if int(volume) < 0:
            dispatcher.utter_message("시스템 볼륨은 0 보다 작을수 없습니다")
        elif int(volume) > 100:
            dispatcher.utter_message("시스템 볼륨은 100 보다 클수 없습니다")
        else:
            dispatcher.utter_message("시스템 볼륨을 {} 으로 내립니다".format(volume))
        return []
