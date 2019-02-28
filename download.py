import requests
import sys

def download_file_from_google_drive(id, destination):
	URL = "https://drive.google.com/open?id=1QuWUeDkXz_AZ027n3GHbM28jVbaxI66E"

	session = requests.Session()

	response = session.get(URL, params = { 'id' : id }, stream = True)
	token = get_confirm_token(response)

	if token:
		params = { 'id' : id, 'confirm' : token }
		response = session.get(URL, params = params, stream = True)

	save_response_content(response, destination)    

def get_confirm_token(response):
	for key, value in response.cookies.items():
		if key.startswith('download_warning'):
			return value

	return None

def save_response_content(response, destination):
	CHUNK_SIZE = 32768

	with open(destination, "wb") as f:
		for chunk in response.iter_content(CHUNK_SIZE):
			if chunk:
				f.write(chunk)

if __name__ == "__main__":

	
	outputFileName = "kishoreresume"
	googleFileID = "1QuWUeDkXz_AZ027n3GHbM28jVbaxI66E"

	inputLine = sys.argv[1]
	if len(sys.argv) == 2:
 		download_file_from_google_drive(googleFileID, outputFileName)
 		print ('Download Complete!')



