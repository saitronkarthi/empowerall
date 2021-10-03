import time
import boto3


def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='mpeg',
        LanguageCode='en-US'
    )

def main():
    transcribe_client = boto3.client('transcribe')
    file_uri = 's3://vdado/audio/DeepLearning_English.mp3'
    transcribe_file('DeeplearningTranscription', file_uri, transcribe_client)


if __name__ == '__main__':
    main()