
from video_recorder import Record
def record_video(request):
    if request.config.getoption('--record_vid') == 'true':
        recorder = Record(driver, file_name=f'{file_path("videos")}/{test_name}_video')
        recorder.start()
        yield
        recorder.stop()
    else:
        yield