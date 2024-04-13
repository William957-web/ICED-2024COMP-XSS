import selenium
from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
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
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")  
        opts.add_argument("--disable-gpu") 
        opts.add_argument("--disable-extensions")
        opts.add_argument("--disable-infobars")
        opts.add_argument("--start-maximized")
        opts.add_argument("--disable-notifications")
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        service = Service(executable_path=ChromeDriverManager().install())
        content=request.form['content']
        content=content.replace('%3C', '').replace('%3c', '').replace('%3E', '').replace('%3e', '').replace('<', '').replace('>', '')
        browser = webdriver.Firefox(service=service, options=opts)
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
