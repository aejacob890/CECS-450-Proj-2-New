class Gaze_Data_Line:
    def __init__(self, id, time, dur, horizontal, vertical):
        self.id_num = id
        self.timestamp = time
        self.duration = dur
        self.gaze_x = horizontal
        self.gaze_y = vertical

    def __str__(self):
        return "Gaze #" + str(self.id_num) + "--- Timestamp: " + str(self.timestamp) + "; Duration: " \
               + str(self.duration) + "; X: " + str(self.gaze_x) + "; Y: " + str(self.gaze_y)

    def get_id_num(self):
        return self.id_num

    def get_timestamp(self):
        return self.timestamp

    def get_duration(self):
        return self.timestamp

    def get_gaze_x(self):
        return self.gaze_x

    def get_gaze_y(self):
        return self.gaze_y
    