import os
import signal
import sys
import time

try:
    # Python 3+
    from urllib.request import urlretrieve, urlopen
except ImportError:
    # Python 2
    from urllib import urlretrieve
    from urllib2 import urlopen

latest_gecko_driver = '0.18.0'

def get_remote_binary(whichbin):
    # if not which(whichbin):
    print("=" * 80)
    print("PyWebRunner can try to download the correct driver automatically.")
    fixit = yn("Would you like for PyWebRunner to attempt to fix this for you? [Y/N]: ")
    if fixit:

        latest_chrome_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        latest_chrome_version = '2.31'

        pathdirs = [p for p in os.environ[
            'PATH'].split(':') if os.access(p, os.W_OK)]
        if '/usr/local/bin' in pathdirs:
            base_path = '/usr/local/bin'
        else:
            print(
                "The following directories are in your path and appear to be writable: ")
            for p in pathdirs:
                print(p)
            print("Which of those directories would you like to use?")
            answer = get_input("Hit the enter key to cancel.")
            if answer:
                if answer in pathdirs:
                    base_path = answer
                else:
                    print("Oops... that path is not in the list. Aborting.")
                    sys.exit(1)
            else:
                print("Aborting.")
                sys.exit(1)

        if whichbin == 'wires':
            available_binaries = {
                'arm7hf': 'https://github.com/mozilla/geckodriver/releases/download/v{}/geckodriver-v{}-arm7hf.tar.gz'.format(latest_gecko_driver, latest_gecko_driver),
                'linux64': 'https://github.com/mozilla/geckodriver/releases/download/v{}/geckodriver-v{}-linux64.tar.gz'.format(latest_gecko_driver, latest_gecko_driver),
                'mac': 'https://github.com/mozilla/geckodriver/releases/download/v{}/geckodriver-v{}-macos.tar.gz'.format(latest_gecko_driver, latest_gecko_driver),
                'win64': 'https://github.com/mozilla/geckodriver/releases/download/v{}/geckodriver-v{}-win64.zip'.format(latest_gecko_driver, latest_gecko_driver)
            }
        else:
            try:
                latest_chrome_version = urlopen(latest_chrome_url).read().strip()
            except StandardError:
                pass

            try:
                latest_chrome_version = str(latest_chrome_version, 'utf-8')
            except StandardError:
                pass

            available_binaries = {
                'linux32': 'http://chromedriver.storage.googleapis.com/{}/chromedriver_linux32.zip'.format(latest_chrome_version),
                'linux64': 'http://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip'.format(latest_chrome_version),
                'mac64': 'http://chromedriver.storage.googleapis.com/{}/chromedriver_mac64.zip'.format(latest_chrome_version),
                'win32': 'http://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip'.format(latest_chrome_version),
            }

        print("Which of these fits your system?")
        for k in available_binaries:
            print(k)

        answer = get_input("Choose one or hit enter to abort: ")
        if answer and available_binaries.get(answer):
            # if whichbin == 'wires':
            #     download_driver_file(whichbin, available_binaries[answer], base_path)
            #     latest = "https://github.com/mozilla/geckodriver/releases/download/v{}/geckodriver-v{}-macos.tar.gz".format(latest_gecko_driver)
            #     download_driver_file(whichbin, latest, base_path)
            # else:
            download_driver_file(whichbin, available_binaries[answer], base_path)
            print("Done! You should be able to use the driver now.")

def download_driver_file(whichbin, url, base_path):
    if url.endswith('.tar.gz'):
        ext = '.tar.gz'
    else:
        ext = '.zip'
    print("Downloading from: {}".format(url))
    download_file(url, '/tmp/pwr_temp{}'.format(ext))
    if ext == '.tar.gz':
        import tarfile
        tar = tarfile.open('/tmp/pwr_temp{}'.format(ext), "r:gz")
        tar.extractall('{}/'.format(base_path))
        tar.close()
    else:
        import zipfile
        with zipfile.ZipFile('/tmp/pwr_temp{}'.format(ext), "r") as z:
            z.extractall('{}/'.format(base_path))

    # if whichbin == 'wires' and '/v{}/'.format(latest_gecko_driver) in url:
    #     os.rename('{}/geckodriver'.format(base_path),
    #               '{}/wires'.format(base_path))
    #     os.chmod('{}/wires'.format(base_path), 0o775)
    if whichbin == 'wires':
        os.chmod('{}/geckodriver'.format(base_path), 0o775)
    else:
        os.chmod('{}/chromedriver'.format(base_path), 0o775)

def fix_firefox():
    print("You are running FireFox >= 48.0.0")
    print("This means you need geckodriver: https://github.com/mozilla/geckodriver/releases")
    print("(If using selenium==2.x.x Be sure and rename the executable to \"wires\" instead of geckodriver")
    print("and put it in your path.)")
    get_remote_binary('wires')

def fix_gecko():
    get_remote_binary('wires')

def fix_chrome():
    print("You are running Chrome")
    print("This means you need chromedriver: https://sites.google.com/a/chromium.org/chromedriver/downloads")
    get_remote_binary('chromedriver')


def download_file(url, destination):
    return urlretrieve(url, destination)


def yn(question):
    return get_input(question).lower().strip()[0] == "y"


def prompt(question):
    return get_input('{}: '.format(question))


def get_input(question):
    py3=sys.version_info[0] > 2

    if py3:
        response=input(question)
    else:
        response=raw_input(question)

    return response


class Timeout():
    """
    Timeout class using ALARM signal.
    Used to Timeout the loading of the Firefox driver if we are > Firefox 48
    """
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec=sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)  # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


def which(cmd, mode=os.F_OK | os.X_OK, path=None):
    try:
        from shutil import which
        return which(cmd, mode=mode, path=path)
    except ImportError:
        # Check that a given file can be accessed with the correct mode.
        # Additionally check that `file` is not a directory, as on Windows
        # directories pass the os.access check.
        def _access_check(fn, mode):
            return (os.path.exists(fn) and os.access(fn, mode)
                    and not os.path.isdir(fn))

        # If we're given a path with a directory part, look it up directly rather
        # than referring to PATH directories. This includes checking relative to the
        # current directory, e.g. ./script
        if os.path.dirname(cmd):
            if _access_check(cmd, mode):
                return cmd
            return None

        if path is None:
            path=os.environ.get("PATH", os.defpath)
        if not path:
            return None
        path=path.split(os.pathsep)

        if sys.platform == "win32":
            # The current directory takes precedence on Windows.
            if not os.curdir in path:
                path.insert(0, os.curdir)

            # PATHEXT is necessary to check on Windows.
            pathext=os.environ.get("PATHEXT", "").split(os.pathsep)
            # See if the given file matches any of the expected path extensions.
            # This will allow us to short circuit when given "python.exe".
            # If it does match, only test that one, otherwise we have to try
            # others.
            if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
                files=[cmd]
            else:
                files=[cmd + ext for ext in pathext]
        else:
            # On other platforms you don't have things like PATHEXT to tell you
            # what file suffixes are executable, so just pass on cmd as-is.
            files=[cmd]

        seen=set()
        for dir in path:
            normdir=os.path.normcase(dir)
            if not normdir in seen:
                seen.add(normdir)
                for thefile in files:
                    name=os.path.join(dir, thefile)
                    if _access_check(name, mode):
                        return name
        return None
