# Alia
human interface python - google speek
- tray icon application - check
- splash screen class - check

# Install python 3.7.4 modules:

PyQt5, SpeechRecognition

example:

- [mythcat@desk ~]$ pip3 install SpeechRecognition --user

# Install pyaudio on Fedora

- need to use dnf tool ( pip cannot compile this python module)

[root@desk mythcat]# dnf search python3-pyaudio

Last metadata expiration check: 0:12:34 ago on Sat 17 Aug 2019 02:57:00 PM EEST.

=========================================== Name Exactly Matched: python3-pyaudio ===========================================

python3-pyaudio.x86_64 : Python bindings for PortAudio

[root@desk mythcat]# dnf install python3-pyaudio

...

Installed:
  python3-pyaudio-0.2.11-2.fc30.x86_64                              portaudio-19-29.fc30.x86_64                             

Complete!

- test with python:

Python 3.7.4 (default, Jul  9 2019, 16:32:37) 
[GCC 9.1.1 20190503 (Red Hat 9.1.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyaudio
>>> 


# Notes
- the project is old
- some of my files are gone
- I will try to restore it in time.
