from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
from PyQt5.Qt import Qt
from subscriberqt import QtSubscriber
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

class Log:
    def __init__(self, message, manual_action = 0 ):
        self.message = message 
        self.manual_action = manual_action

class TaskVideo(QtSubscriber):

    sig_image = pyqtSignal(QImage)
    sig_read = pyqtSignal(str)
    sig_start = pyqtSignal(int)
    sig_stop = pyqtSignal(int)
   
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.cancelar = 0
    
    #listener
    def show_log(self, message, manual_action = 0):
        self.sig_log.emit(Log(message, manual_action))
    

    #listener
    def update_image(self, image):        
        self.sig_image.emit(image)


    def cancel_video(self, cancelar):
        self.cancelar = cancelar
  

    def run(self):
        vs = VideoStream(src=0).start()
        #time.sleep(2.0)
        
        self.sig_start.emit(1)

        while True:

            try:
           
                frame = vs.read()
                frame = imutils.resize(frame, width=640, height=300)
                barcodes = pyzbar.decode(frame)
                
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = rgbImage.shape
                bytesPerLine = channel * width
                convertToQtFormat = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
                image = convertToQtFormat.scaled(640, 360, Qt.KeepAspectRatioByExpanding)
                self.update_image(image)

                for barcode in barcodes:
                    

                    try:
                        barcodeData = barcode.data.decode("utf-8")		            
                        chave = str(barcodeData).split("|")[0].replace("CFe","")
                        self.sig_read.emit(chave)

                        #desenha retangulo na tela
                        try:  


                            (x, y, w, h) = barcode.rect
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(frame, chave, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                            #atualiza tela novamente
                            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            height, width, channel = rgbImage.shape
                            bytesPerLine = channel * width
                            convertToQtFormat = QImage(rgbImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
                            image = convertToQtFormat.scaled(640, 360, Qt.KeepAspectRatioByExpanding)
                            self.update_image(image)

                        except Exception as err2:
                            print('ERROR on trying to draw rectangle: ' + repr(err2))
                        
                        print('Chave de Acesso: ' + str(barcode.type) + " - " + chave)
                    except Exception as err  : 
                        print('ERROR: ' + repr(err))

                if (self.cancelar):
                    print("Finalizando captura de vídeo...")
                    #cv2.close()
                    #cv2.destroyAllWindows()
                    vs.stop()
                    #self.terminate()
                    self.sig_stop.emit(1)	
                    self.quit()
                    
                    break
                                    
            except Exception as errMain:
                 print('ERROR: ' + repr(errMain))