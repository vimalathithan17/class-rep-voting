from django.shortcuts import render,redirect
from django.http import HttpResponse
from candidatereg.models import Candidates
from voter.models import VoterList
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
import cv2
from pyzbar import pyzbar
from django.contrib import messages




def decode_barcode(frame):
    # Find and decode barcodes
    barcodes = pyzbar.decode(frame)

    # Process each barcode found
    for barcode in barcodes:
        # Extract the bounding box location of the barcode
        (x, y, w, h) = barcode.rect

        # Draw a rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Convert barcode data to string format
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Print barcode information
        print(barcode_data)
        #print("Barcode Type:", barcode_type)
        return barcode_data  # Set flag to True if a barcode is detected

    return False  # Set flag to False if no barcode is detected

def main():
    # Initialize the video stream
    video_capture = cv2.VideoCapture(0)

    barcode_detected = False  # Flag to track if barcode is detected

    while True:
        # Read the current frame from the video stream
        ret, frame = video_capture.read()

        # Resize the frame for better processing speed
        frame = cv2.resize(frame, None, fx=0.6, fy=0.6)

        # Convert the frame to grayscale for barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Call the barcode decoding function
        barcode_detected = decode_barcode(gray)

        # Display the resulting frame
        cv2.imshow("Barcode Scanner", frame)

        # Exit the loop if barcode is detected and processed
        if barcode_detected:
            break

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
    return barcode_detected
def voting(request):

    if request.method=='GET':
        voter_roll_no=request.GET['rollno']
        voter=VoterList.objects.get(rno=voter_roll_no)
        if voter.voted :
            return HttpResponse("You Have Already Casted Your Vote")
        else:
            candidates=Candidates.objects.all() 
            template='voting/voting.html'
            data={'candidates':candidates,'roll_no':voter_roll_no}
            return  render( request,template,data)
    print(request.method)
    if request.method=='POST':
        print(request.POST)
        rno=request.POST['rollno']
        voter=VoterList.objects.get(rno=rno)
        print(request.POST)
        voted_roll_no=request.POST['choice']
        voted_candidate=Candidates.objects.get(roll_no=voted_roll_no)
        voted_candidate.votes+=1
        voted_candidate.save()
        voter.voted=True
        voter.save()
        messages.success(request,"Your Vote Has Been Successfully Casted")
        return redirect("homepage:home")
def voter_check(request):
        
        if request.method=='GET':
            voter_roll_no=main()
            voter=VoterList.objects.get(rno=voter_roll_no)
            
            if voter.voted:
                 messages.success(request,"You have already casted your vote")
                 return redirect('homepage:home')
            else:

                template='voting/voter_details.html'
                data={'voter':voter,'roll_no':voter_roll_no}
                return  render( request,template,data)
        
