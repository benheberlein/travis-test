from flask import Flask, render_template, request

def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        return render_template('index.html', converted='')

    @application.route('/', methods=['POST'])
    def index_post():
        text = request.form['text']
        base = request.form['base']
        if verify(text) == True and verify_base(base) == True:
            num = to_int(text)
            b = to_int(base)
            return render_template('index.html', converted=convert_wrap(num, b))
        else:
            return render_template('index.html', converted="BAD INPUT")

    return application


def verify(text):
    '''This function verifies that the input is well formatted.'''
    try:
        t = int(text)
        if t >= 0:
            return True
    except ValueError:
        return False   

    return False


def verify_base(base):
    '''This function verifies that the base is well formatted and 
       within bounds 2 to 16.'''

    try:
        b = int(base)
        if b >= 2 and b <= 16:
            return True
    except ValueError:
        return False

    return False

def to_int(s):
    '''This function converts a string number to an integer.'''
    return int(s)

def convert_wrap(num, base):
    ''' This function wraps a base conversion in an appropriate 0x prepend.'''

    pre = "__btqpshonduvwyzx"

    return "0" + pre[base] + " " + convert(num, base)

def convert(num, base):
    '''This function converts to the appropriate base.
       The function could just use hex() but we implement
       it with a custom recursive function in order to
       demonstrate the testing framework.'''
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    else:
        return convert(num // base, base) + digits[num % base]
    
if __name__ == "__main__":
    application = create_app()
    application.run(port=80)
