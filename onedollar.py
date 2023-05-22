import string
import cv2
from dollarpy import Recognizer, Template, Point
from abc import ABC, abstractmethod
import numpy as np
from scipy.spatial.distance import euclidean


class TrajectoryClasificationStrategy(ABC):

    @abstractmethod
    def startTrajectoy(self, points):
        pass


class OneDollarRecognizer(TrajectoryClasificationStrategy):
    def startTrajectoy(self, points):
        z = []

        template_no = Template("no", [ Point(82,104), Point(83,104), Point(84,104), Point(86,104), Point(90,103), Point(94,103), Point(98,102), Point(102,101), Point(106,101), Point(110,100), Point(114,99), Point(116,99), Point(118,99), Point(121,98), Point(122,98), Point(125,98), Point(127,98), Point(129,98), Point(132,98), Point(135,99), Point(141,101), Point(146,102), Point(152,104), Point(158,105), Point(162,107), Point(166,107), Point(170,108), Point(174,108), Point(177,109), Point(180,110), Point(182,110), Point(184,110), Point(186,110), Point(189,111), Point(192,112), Point(194,112), Point(197,113), Point(198,113), Point(199,114), Point(198,114), Point(197,114), Point(194,115), Point(193,115), Point(191,116), Point(186,117), Point(181,118), Point(178,118), Point(177,118), Point(175,118), Point(173,118), Point(170,118), Point(153,118), Point(152,118), Point(151,118), Point(150,118), Point(145,117), Point(138,117), Point(133,116), Point(129,116), Point(128,116), Point(127,116), Point(126,116), Point(125,116), Point(122,115), Point(118,115), Point(115,115), Point(112,115), Point(110,115), Point(109,115), Point(107,115), Point(106,115), Point(104,115), Point(102,115), Point(101,115), Point(100,115), Point(99,115)])
        template_yes = Template("yes", [ Point(124,81), Point(124,82), Point(124,83), Point(124,84), Point(125,86), Point(125,89), Point(125,92), Point(128,104), Point(130,113), Point(132,122), Point(133,129), Point(133,134), Point(133,138), Point(133,137), Point(133,136), Point(134,130), Point(135,124), Point(136,119), Point(136,116), Point(137,115), Point(137,112), Point(137,111), Point(137,110), Point(137,108), Point(137,106), Point(138,106), Point(138,104), Point(138,103), Point(139,102), Point(139,99), Point(139,98), Point(139,96), Point(139,94), Point(139,91), Point(139,90), Point(139,87), Point(139,85), Point(139,84), Point(139,83)])
        template_straight = Template("straight", [ Point(129,130), Point(130,130), Point(131,130), Point(131,129), Point(132,129), Point(133,129), Point(134,129), Point(133,129), Point(132,130), Point(133,130), Point(134,130), Point(137,129), Point(141,129), Point(139,129), Point(138,129), Point(137,130), Point(136,131), Point(135,131), Point(134,131), Point(135,131), Point(136,131), Point(137,130)])
        recognizer = Recognizer([template_no,template_yes])
        for pt in points:
            x, y = pt
            z.append(Point(x, y))
        # Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.
        result = recognizer.recognize(z)
        shape, conf = result
        # if (shape != None):
        #     print("1$ ==> ", result)  # Output: ('X', 0.733770116545184)

        return result

class TrajectoryClasification:
    def __init__(self, trajectoryStrategyType: TrajectoryClasificationStrategy):
        self.pointsList = []
        self.confidence = []
        self.trajectoryStrategyType = trajectoryStrategyType

    def trajectoryType(self):
        chossenTypeResuts = self.trajectoryStrategyType.startTrajectoy(self.pointsList)

        return chossenTypeResuts

    def getPoints(self):
        return self.pointsList

    def resetPoints(self):
        self.pointsList = []

    def numberOfPoints(self):
        return len(self.pointsList)

    def determineTheCenter(self, frame, cnts):
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        cv2.circle(frame, center, 2, (0, 0, 255), -1)
        self.pointsList.append(center)
        # print(center)
        return center
    def append_to_list(self,Point):
        self.pointsList.append(Point)