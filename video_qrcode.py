from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

vs = VideoStream(src=0).start()
time.sleep(2.0)


while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=921, height=331)
	barcodes = pyzbar.decode(frame)

	for barcode in barcodes:
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		print(str(barcodeData).split("|")[0].replace("CFe",""))
		
	#cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()	