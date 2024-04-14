import selenium
from selenium import webdriver
import time 
from flask import *
url = "https://iced-2024comp-xss-onrender-com.onrender.com/?content="
app = Flask(__name__)



@app.route('/')
def main():
    response=make_response(render_template('index.html'))
    return response

@app.route('/g3tcookieeee')
def getcookie():
    response=make_response(render_template('index.html'))
    response.set_cookie('flag', 'ICED{XsS_repl@c3_WAf_c4n_B33_easily_pwned}')
    return response

@app.route('/visit',  methods=['GET', 'POST'])
def visit():
    if request.method == 'POST':
        content=request.form['content']
        content=content.replace('%3C', '').replace('%3c', '').replace('%3E', '').replace('%3e', '').replace('<', '').replace('>', '')
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.javascriptEnabled"] = True
        cap["phantomjs.page.settings.loadImages"] = True
        cap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'], desired_capabilities=cap)
        browser.get("https://iced-2024comp-xss-onrender-com.onrender.com/g3tcookieeee")
        time.sleep(5)
        browser.get(url+content)
        #cookies=browser.get_cookies()
        time.sleep(5)
        browser.quit()
        return f"<h1>Admin have visited it!</h1><br>Final URL:{url+content}</br>"
    else:
        return "Method not allowed"
    
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
