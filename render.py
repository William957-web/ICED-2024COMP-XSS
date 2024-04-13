import selenium
from selenium import webdriver
import time 
from flask import *
url = "https://iced-2024comp-xss.onrender.com/?content="
app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/visit',  methods=['GET', 'POST'])
def visit():
    if request.method == 'POST':
        content=request.form['content']
        content=content.replace('%3C', '').replace('%3c', '').replace('%3E', '').replace('%3e', '').replace('<', '').replace('>', '')
        browser = webdriver.PhantomJS()
        browser.get(url+content)
        time.sleep(5)
        browser.add_cookie({'name':'flag','value':'ICED{XsS_repl@c3_WAf_c4n_B33_easily_pwned}','path':'/'})
        browser.get(url+content)
        time.sleep(5)
        browser.quit()
        return "Admin will visit it!"
    else:
        return "Method not allowed"
    
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
