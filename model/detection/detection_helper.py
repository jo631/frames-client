from client.model.detection.face_detection.face_detector import FaceDetector

class DetectionHelper:
    def __init__(self):
        self.fd = FaceDetector('client/model/detection/face_detection/deploy.prototxt','client/model/detection/face_detection/res10_300x300_ssd_iter_140000.caffemodel')
        print("DetectionHelper 생성")

    def __del__(self):
        print("DetectionHelper 삭제")

    #return type: None or face Frame(ndarray)
    def detectFaceFromFrame(self, frame,threshold=0.6):

        detection = self.__getFaceDetectionFrom(frame, threshold)

        if detection is None:
            return None

        face = self.__getFaceFrom(detection, frame)

        return face

    #return type: 1-dimension ndarray
    def __getFaceDetectionFrom(self, frame, threshold):
        detections = self.fd.getDetectionsFromFrame(frame)
        detection, confidence = None, 0

        for d in detections:
            c = self.fd.getConfidence(d)
            #TODO 프레임 크기 일정이상 요구할수도 있음 
            if c < threshold:
                continue
            if confidence < c:
                detection = d

        return detection
    
    def __getFaceFrom(self, detection, frame):
        (left,top,right,bottom) = self.fd.getFaceLocation(detection,frame)
        face = frame[top:bottom,left:right]
        return face

    # def __isMasked(self, face):
    #     mask, withoutMask = self.md.maskDetection(face)
    #     if(mask>withoutMask):
    #         return True
    #     else:
    #         return False

    # def __getLandmarkBy(self, face):
    #     return LandmarkDetector.getLandmarkBy(face)
