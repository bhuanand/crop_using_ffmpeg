import sys
import os
import subprocess
import shutil
import tempfile

def get_hms(time):
    hms = time.split(":")
    if len(hms) == 1:
        return "00:00:" + time
    elif len(hms) == 2:
        return "00:" + time
    else:
        return time

def crop_and_save(from_slice, to_slice, filename):
    file_one = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
    file_two = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
    file_three = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
    
    command_one = ["ffmpeg",
                   "-y",
                   "-i",
                   filename,
                   "-ss",
                   "00:00:00",
                   "-to",
                   str(get_hms(from_slice)),
                   "-strict",
                   "-2",
                   file_one.name]

    command_two = ["ffmpeg",
                   "-y",
                   "-i",
                   filename,
                   "-ss",
                   str(get_hms(to_slice)),
                   "-strict",
                   "-2",
                   file_two.name]

    command_three = ["ffmpeg",
                     "-y",
                     "-i",
                     file_one.name,
                     "-i",
                     file_two.name,
                     "-filter_complex",
                     "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]",
                     "-map",
                     "[v]",
                     "-map",
                     "[a]",
                     "-strict",
                     "-2",
                     file_three.name]

    print(command_one)
    print(command_two)
    print(command_three)
    
    try:
        subprocess.check_call(command_one)
        subprocess.check_call(command_two)
        subprocess.check_call(command_three)

        shutil.move(file_three.name, filename)
    except Exception as e:
        print(e)
    finally:
        os.unlink(file_one.name)
        os.unlink(file_two.name)
        if os.path.exists(file_three.name):
            os.unlink(file_three.name)
