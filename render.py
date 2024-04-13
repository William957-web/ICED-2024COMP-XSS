import selenium
from selenium import webdriver  
from selenium.common.exceptions import WebDriverException
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
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        content=request.form['content']
        content=content.replace('%3C', '').replace('%3c', '').replace('%3E', '').replace('%3e', '').replace('<', '').replace('>', '')
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)
        browser.get(url+content)
        browser.add_cookie({'name':'flag','value':'ICED{XsS_repl@c3_WAf_c4n_B33_easily_pwned}','path':'/'})
        browser.get(url)
        time.sleep(2)
        browser.quit()
        return "Admin will visit it!"
    else:
        return "Method not allowed"
    
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
