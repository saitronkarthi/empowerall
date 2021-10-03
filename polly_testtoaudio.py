import boto3
import json
s3 = boto3.resource("s3")
pollyclient = boto3.client('polly')
content_object = s3.Object('vdado/translatedtranscript', 'deeplearningtranslated.json')
file_content = content_object.get()['Body'].read().decode('utf-8')
json_content = json.loads(file_content)
tosynthesize=json_content['TranslatedText'])
response = pollyclient.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = tosynthesize,
                Engine = 'neural')

file.write(response['AudioStream'].read())
file.close()
bucket_name = "vdado"
file_name = "deeplearning_spanish.mp3"
s3_path = "translatedaudio/" + file_name
s3.Bucket(bucket_name).put_object(Key=s3_path, Body=response)
