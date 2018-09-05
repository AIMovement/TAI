# T[UG] AI
Repository for Semcon AI TUG sessions

## Tutorial
This section describes needed packages/tools for the repository.

### Git
If developing on windows, [Git bash](https://git-scm.com/download/win) is
recommended. It includes a small Linux-like environment based on
[MSYS2](http://www.msys2.org/) (which in turn is based on
[Cygwin](https://www.cygwin.com/).)


### Python 3.6
Ensure that you have __Python 3.6__ installed on your laptop. You can check you python 3.x version by:
```
python3 -v
```

If you do not have it, then here is a link that might help you install python 3.6:

[Install instructions for Python 3.x](https://realpython.com/installing-python/)

### Tox
Ensure that you have __tox__ package installed. 
```
pip3 install tox
```
Tox [docs](https://tox.readthedocs.io/en/latest/).

### Voice recording using sox & rec
´´´
rec -r 16000 -c 1 test1.wav silence 1 0.1 3% 1 3.0 3%
´´´
This command is executed on the command line using python [subprocess](https://docs.python.org/3/library/subprocess.html)
´´´
p = subprocess.Popen(["rec", "test.wav", "-c", "1", "-r", "16000", "silence", "1", "0.1", "3%", "1", "3.0", "3%"],stdout=subprocess.PIPE)
´´´
The recording automatically stops when detects a silence of 3 secs. Source [stackoverflow](https://unix.stackexchange.com/questions/55032/end-sox-recording-once-silence-is-detected/57593).
