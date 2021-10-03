import json
import boto3
from urllib.parse import urlparse, unquote
from pathlib import Path
def lambda_handler(event, context):

    targetLang = "es"
    strPath='s3://vdado/transcript/'
    s3Key = str(Path(strPath)).relative_to('/')
    s3 = boto3.resource('s3')
    s3Obj = 'deeplearningtranscrition'
    srcText = s3Obj['Body'].read()
    srcText = srcText.decode('utf-8')
    translateClient = boto3.client('translate')
    response = translateClient.translate_text(
                                                Text = srcText,
                                                SourceLanguageCode='en',
                                                TargetLanguageCode=targetLang)
    s3_path='transcript/deeplearningtranslated'
    s3.Bucket('vdado').put_object(Key=s3_path, Body=encoded_string)
    