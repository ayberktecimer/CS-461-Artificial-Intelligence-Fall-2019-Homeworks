import cv2

class Visualization:

    def __init__(self):
        self.river_img = cv2.imread("river.png")

    def draw_state(self, state):

        res = self.river_img.copy()

        # Get the details of the state
        number_of_missionaries = state.m
        number_of_cannibals = state.c
        boat_location = state.b

        # Check the location of the boat
        if boat_location == 1:
            people_movement, boat_movement = 0, 0
        else:
            people_movement, boat_movement = 300, 100

        # Draw missionaries
        for i in range(number_of_missionaries):
            org = (20 + people_movement, 80 + i * 60)
            font = cv2.FONT_HERSHEY_COMPLEX
            font_scale = 1
            color = (255, 0, 0)
            cv2.putText(res, "M", org, font, font_scale, color)

        # Draw cannibals
        for i in range(number_of_cannibals):
            org = (60 + people_movement, 80 + i * 60)
            font = cv2.FONT_HERSHEY_COMPLEX
            font_scale = 1
            color = (0, 0, 255)
            cv2.putText(res, "C", org, font, font_scale, color)

        # Draw the boat
        pt1, pt2 = (boat_movement + 130, 200), (boat_movement + 160, 230)
        color = (120, 255, 255)
        cv2.rectangle(res, pt1, pt2, color=color, thickness=cv2.FILLED)

        frame_name = str(number_of_missionaries) + "M" + str(number_of_cannibals) + "C" + str(boat_location)
        cv2.imshow(frame_name, res)
        cv2.waitKey(0)