import semail
import takepic
import os

if __name__ == '__main__':
    filename = takepic.takepic()
    semail.sendEmail2("", "Pi Pic", [filename])
    # we do not want to keep the pics if the
    # email is success.
    os.remove(filename)
