from parser_m.date import Date


class Day:
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    def __init__(self):
        self.date = Date()

        # Constant fields
        self._TODAY_DAY = self.date.get_day_of_week().strip()
        self._TODAY_WEEK_PARITY = self.date.get_week_parity()

        # Fields with current working values
        self._current_day = self._TODAY_DAY
        self._current_week_parity = self._TODAY_WEEK_PARITY

    def _set_day(self, next_day_value: int):
        """Set day of week and week parity to day + $next_day_value"""
        for day_index in range(7):
            if self.days[day_index] == self._TODAY_DAY:
                self._current_day = self.days[(day_index + next_day_value) % 7]
                if ((day_index + next_day_value) // 7) % 2 == 1:
                    self._change_week_parity()

    def _reset_all_values(self):
        """Reset all changed values to current days values"""
        self._current_day = self._TODAY_DAY
        self._current_week_parity = self._TODAY_WEEK_PARITY

    def test(self):
        print(self._current_week_parity, self._current_day)
        print(self._current_week_parity, self._current_day)

    def _change_week_parity(self):
        if self._current_week_parity == "Четная":
            self._current_week_parity = "Нечетная"
        else:
            self._current_week_parity = "Четная"

    def get_day(self, next_day_value: int = 0):
        self._set_day(next_day_value)
        r = self._current_day
        self._reset_all_values()
        return r

    def get_parity(self, next_day_value: int = 0):
        self._set_day(next_day_value)
        r = self._current_day
        self._reset_all_values()
        return r

    def get_day_parity(self, next_day_value: int = 0):
        self._set_day(next_day_value)
        r = [self._current_day, self._current_week_parity]
        self._reset_all_values()
        return r

    # Methods to test the class
    def get_today_day(self): return self._TODAY_DAY

    def get_today_week_parity(self): return self._TODAY_WEEK_PARITY

    def get_current_day(self): return self._current_day

    def get_current_week_parity(self): return self._current_week_parity
