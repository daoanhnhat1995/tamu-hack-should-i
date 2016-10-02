import httplib2
import json 
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

#https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/language/api/analyze.py
def get_service():
    credentials = GoogleCredentials.get_application_default()
    scoped_credentials = credentials.create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    scoped_credentials.authorize(http)
    return discovery.build('language', 'v1beta1', http=http)

def analyze_syntax(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'features': {
            'extract_syntax': True,
        },
        'encodingType': encoding,
    }

    service = get_service()

    request = service.documents().annotateText(body=body)
    response = request.execute()

    return response



if __name__ == '__main__':
        response = analyze_syntax("Should i go out and eat at six street downtown, i dont know")
        print(json.dumps(response, indent=2))




