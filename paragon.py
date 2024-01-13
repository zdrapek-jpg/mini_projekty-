import pytesseract
import imutils
import cv2
import re
import pyperclip

print(f" aktualna wersja pytesseract : {pytesseract.get_tesseract_version()}")
into = input("nazwa obrazu")
orig = cv2.imread(into)
image = orig.copy()
image = imutils.resize(image, width=500)
ratio = orig.shape[1] / float(image.shape[1])
# convert the image to grayscale, blur it slightly, and then apply
# edge detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 200)
# check to see if we should show the output of our edge detection
# procedure
debug = 1
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)


# initialize a contour that corresponds to the receipt outline
receiptCnt = None
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# if our approximated contour has four points, then we can
	# assume we have found the outline of the receipt
	if len(approx) == 4:
		receiptCnt = approx
		break
# if the receipt contour is empty then our script could not find the
# outline and we should be notified
if receiptCnt is None:
	raise Exception(("Could not find receipt outline. "
		"Try debugging your edge detection and contour steps."))


# check to see if we should draw the contour of the receipt on the
# image and then display it to our screen
if debug> 0:
	output = image.copy()
	cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)
# apply a four-point perspective transform to the *original* image to
# obtain a top-down bird's-eye view of the receipt


# apply OCR to the receipt image by assuming column data, ensuring
# the text is *concatenated across the row* (additionally, for your
# own images you may need to apply additional processing to cleanup
# the image, including resizing, thresholding, etc.)
options = "--oem 3 --psm 4 -l pol"
text = pytesseract.image_to_string(
	cv2.cvtColor(output, cv2.COLOR_BGR2RGB),
	config=options)
# show the raw output of the OCR process
print("[INFO] raw output:")
print("==================")
print(text)
pyperclip.copy(text)
pattern = r"\d+\s*x\d+(?:\.\d+)?"

new = []
# receipt

for row in text.split("\n"):
    if re.search(pattern, row) is not None:
        new.append(row)

text_list = list(new)


numbers_list = []
text_lists =[]
dict_number = {}
dict_items = {}
i =0
for linia in text_list:
    # Wyszukiwanie pierwszego wystąpienia liczby w tekście
    match = re.search(r'\d+.*?$', linia)
    if linia =="":
        continue
    if match:
        # Pobranie znalezionego dopasowania
        number = match.group()
        # Dodanie liczby do listy
        numbers_list.append(number)
        dict_number['ilosc'+str(i)] = number
    else:
        dict_number['ilosc'+str(i)] = 0



    match = re.search(r'(.*?)\d+', linia)

    if match:
        # Pobranie znalezionego dopasowania
        extracted_text = match.group(1)
        # Dodanie tekstu do listy
        text_lists.append(str(extracted_text))
        dict_items['item'+str(i)] = extracted_text
    else:
        dict_number['ilosc'+str(i)] = None

    i+=1

dict_end= {}
keys=[]
values= []
for co_k,co_v in dict_items.items():
    keys.append(co_v)
for  ilos_k,value_v in dict_number.items():
    values.append(value_v)

for i in range(len(values)-1):
    dict_end[str(keys[i])] = values[i]


for linia in text.split("\n"):
    match = re.search(r"SUMA\s*PLN\s*",linia)
    if match:

        text_list.append(linia)
        dopasuj = re.search(r"\b\d{1,3}(?:\s?\d{3})*(?:,\d{1,2})?,\d{1,3}(?:\s?\d{3})*(?:,\d{1,2})?\b",linia)
        number = dopasuj.group()
        dict_end["SUMA PLN"]=number
for k,v in dict_end.items():
    print(f"{k} : {v}")

