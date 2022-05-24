import pytest
import random
import string
import platform

class YouMessedUpError(NotImplementedError):
    pass

def filter_filename(fname):

    ilegal_chars = ['<', '>', '"', ';', ';', ':', ',', '|', '\\', '?', '!', '*']
    for char in ilegal_chars:
        fname = fname.replace(char, '_')

    char_chars = []
    for char in fname:
        if char in string.printable:
            char_chars.append(char)
        else:
            char_chars.append('_')
    fname = "".join(char_chars)

    split_fname = fname.split('/')
    split_fname.pop(0)
    fname = ''
    for split in split_fname:
        to_add = split
        if split[0] == '.': to_add = '_' + split[1:]
        if split[-1] == ' ': to_add = split[:-1] + '_'
        if split[-1] == '.': to_add = split[:-1] + '_'
        fname += '/' + to_add
        
            

    return fname


# Linuxgit

@pytest.mark.skipif(platform.system() not in ["Linux", "Darwin"], reason="POSIX only")
def test_filter_out_illegal_characters_linux():
    assert filter_filename('/home/tuser/normal.txt') == '/home/tuser/normal.txt'
    assert filter_filename('/home/tuser/:colon.txt') == '/home/tuser/_colon.txt'
    assert filter_filename('/home/tuser/;semicolon.txt') == '/home/tuser/_semicolon.txt'
    assert filter_filename('/home/tuser/\\backslash.txt') == '/home/tuser/_backslash.txt'
    assert filter_filename('/home/tuser/!bang.txt') == '/home/tuser/_bang.txt'
    assert filter_filename('/home/tuser/?interro.txt') == '/home/tuser/_interro.txt'
    assert filter_filename('/home/tuser/*asterisk.txt') == '/home/tuser/_asterisk.txt'
    assert filter_filename('/home/tuser/"quote.txt') == '/home/tuser/_quote.txt'
    assert filter_filename('/home/tuser/<lt.txt') == '/home/tuser/_lt.txt'
    assert filter_filename('/home/tuser/>gt.txt') == '/home/tuser/_gt.txt'
    assert filter_filename('/home/tuser/|vbar.txt') == '/home/tuser/_vbar.txt'
    assert filter_filename('/home/tuser/.txt') == '/home/tuser/_txt'

@pytest.mark.skipif(platform.system() not in ["Linux", "Darwin"], reason="POSIX only")
def test_filter_out_non_ascii_characters_linux():
    for i in range(10):
        fname_template = '/home/tuser/%snon_ascii.txt'
        assert filter_filename(fname_template % chr(random.randint(256, 0x1000))) == \
                               fname_template % '_'

@pytest.mark.skipif(platform.system() not in ["Linux", "Darwin"], reason="POSIX only")
def test_filter_initial_period_linux():
    assert filter_filename('/home/tuser/Music/...OK Go/01 Song.ogg') == \
        '/home/tuser/Music/_..OK Go/01 Song.ogg'

@pytest.mark.skipif(platform.system() not in ["Linux", "Darwin"], reason="POSIX only")
def test_filter_end_period_linux():
    assert filter_filename('/home/tuser/Music/OK Go/01 No_ext.') == \
        '/home/tuser/Music/OK Go/01 No_ext_'

@pytest.mark.skipif(platform.system() not in ["Linux", "Darwin"], reason="POSIX only")
def test_filter_end_space_linux():
    assert filter_filename('/home/tuser/Documents/ stuff/doc.txt') == \
        '/home/tuser/Documents/ stuff/doc.txt'
    assert filter_filename('/home/tuser/Documents/stuff /doc.txt') == \
        '/home/tuser/Documents/stuff_/doc.txt'


# Windows

@pytest.mark.skipif(platform.system() not in ["Windows"], reason="Windows only")
def test_filter_out_illegal_characters_windows():
    assert filter_filename('C:\\home\\tuser\\normal.txt') == 'C:\\home\\tuser\\normal.txt'
    assert filter_filename('C:\\home\\tuser\\:colon.txt') == 'C:\\home\\tuser\\_colon.txt'
    assert filter_filename('C:\\home\\tuser\\;semicolon.txt') == 'C:\\home\\tuser\\_semicolon.txt'
    assert filter_filename('C:\\home\\tuser\\\\backslash.txt') == 'C:\\home\\tuser\\_backslash.txt'
    assert filter_filename('C:\\home\\tuser\\!bang.txt') == 'C:\\home\\tuser\\_bang.txt'
    assert filter_filename('C:\\home\\tuser\\?interro.txt') == 'C:\\home\\tuser\\_interro.txt'
    assert filter_filename('C:\\home\\tuser\\*asterisk.txt') == 'C:\\home\\tuser\\_asterisk.txt'
    assert filter_filename('C:\\home\\tuser\\"quote.txt') == 'C:\\home\\tuser\\_quote.txt'
    assert filter_filename('C:\\home\\tuser\\<lt.txt') == 'C:\\home\\tuser\\_lt.txt'
    assert filter_filename('C:\\home\\tuser\\>gt.txt') == 'C:\\home\\tuser\\_gt.txt'
    assert filter_filename('C:\\home\\tuser\\|vbar.txt') == 'C:\\home\\tuser\\_vbar.txt'
    assert filter_filename('C:\\home\\tuser\\.txt') == 'C:\\home\\tuser\\_vbar.txt'

@pytest.mark.skipif(platform.system() not in ["Windows"], reason="Windows only")
def test_filter_out_non_ascii_characters_windows():
    for i in range(10):
        fname_template = 'C:\\home\\tuser\\%snon_ascii.txt'
        assert filter_filename(fname_template % chr(random.randint(256, 0x1000))) == \
                               fname_template % '_'

@pytest.mark.skipif(platform.system() not in ["Windows"], reason="Windows only")
def test_filter_initial_period_windows():
    assert filter_filename('C:\\home\\tuser\\Music\\...OK Go\\01 Song.ogg') == \
        'C:\\home\\tuser\\Music\\_..OK Go\\01 Song.ogg'

@pytest.mark.skipif(platform.system() not in ["Windows"], reason="Windows only")
def test_filter_end_period_windows():
    assert filter_filename('C:\\home\\tuser\\Music\\OK Go\\01 No_ext.') == \
        'C:\\home\\tuser\\Music\\OK Go\\01 No_ext_'

@pytest.mark.skipif(platform.system() not in ["Windows"], reason="Windows only")
def test_filter_end_space_windows():
    assert filter_filename('C:\\home\\tuser\\Documents\\ stuff\\doc.txt') == \
        'C:\\home\\tuser\\Documents\\ stuff\\doc.txt'
    assert filter_filename('C:\\home\\tuser\\Documents\\stuff \\doc.txt') == \
        'C:\\home\\tuser\\Documents\\stuff_\\doc.txt'

