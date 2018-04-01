from google.cloud import speech

client = speech.SpeechClient()
print("line 4")
operation = client.long_running_recognize(
     audio=speech.types.RecognitionAudio(
         uri='gs://my-bucket/recording.flac',
     ),
     config=speech.types.RecognitionConfig(
         encoding='LINEAR16',
         language_code='en-US',
         sample_rate_hertz=44100,
     ),
 )
print("line 13")
op_result = operation.result()
print("line 15")
for result in op_result.results:
    print("line 17")
    for alternative in result.alternatives:
        print('=' * 20)
        print(alternative.transcript)
        print(alternative.confidence)
print("line 22")
