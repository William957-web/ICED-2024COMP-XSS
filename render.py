import selenium
from selenium import webdriver
import time 
from flask import *
url = "https://iced-2024comp-xss-onrender-com.onrender.com/?content="
app = Flask(__name__)



@app.route('/')
def main():
    response=make_response(render_template('index.html'))
    if 'flag' not in request.cookies:
        response.set_cookie('flag', 'Only admin can get it')
    return response

@app.route('/visit',  methods=['GET', 'POST'])
def visit():
    if request.method == 'POST':
        content=request.form['content']
        content=content.replace('%3C', '').replace('%3c', '').replace('%3E', '').replace('%3e', '').replace('<', '').replace('>', '')
        browser = webdriver.PhantomJS()
        browser.get("https://iced-2024comp-xss-onrender-com.onrender.com/")
        time.sleep(5)
        sample={'name': 'flag', 'value': 'ICED{XsS_repl@c3_WAf_c4n_B33_easily_pwned}', 'domain': 'iced-2024comp-xss-onrender-com.onrender.com', 'path': '/'}
        saved_cookie=browser.get_cookies()
        browser.delete_all_cookies()
        for cookie in saved_cookie:
            cookie['domain']='iced-2024comp-xss-onrender-com.onrender.com'
            for k in ('name', 'value', 'domain', 'path', 'expiry'):
                if k in list(cookie.keys()):
                    cookie[k]=sample[k]
            browser.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})
        browser.get(url+content)
        cookies=browser.get_cookies()
        time.sleep(5)
        browser.quit()
        return f"<h1>Admin have visited it!</h1><br>Final URL:{url+content}</br><br>{cookies}</br>"
    else:
        return "Method not allowed"
    
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
