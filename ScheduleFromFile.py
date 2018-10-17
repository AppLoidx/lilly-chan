class ScheduleFromFile:

    @staticmethod
    def get_schedule_from_file(filename, day, week):

        f = open(filename, 'r')
        group_name = f.readline()
        _DAY, _TIME, _WEEK, _AUD, _DIS, _TEACHER = f.readline().split()
        temp = "."
        result = group_name + "\nРасписание на " + day + ":\n\n"
        while (temp[0] != "end"):
            temp = f.readline().split()
            if temp[0] == day and (temp[2] == week or temp[2] == "все"):
                result += _TIME + ": " + temp[1] + "\n" \
                          + _AUD + ": " + temp[3] + "\n" \
                          + _DIS + ": " + temp[4] + "\n" \
                          + _TEACHER + ": " + temp[5]
                result += "\n" + "-----\n"
        return result