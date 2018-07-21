from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context

from vsearch import search4letters

from DBcm import UseDatabase

from checker import check_logged_in

app = Flask(__name__)
app.config['dbconfig'] = { 	'host': '127.0.01',
				'user': 'vsearch',
				'password': 'vsearchpasswd',
				'database': 'vsearchlogDB', 
			}


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return render_template('results.html',
            the_phrase=phrase,
            the_letters=letters,
            the_title=title,
            the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

""" Our previous log_request function, which logs into the simple log file

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

Below is our new log_request function which is using the database and context manager
"""

def log_request(req: 'flask_request', res: str) -> None:
	with UseDatabase(app.config['dbconfig']) as cursor:
		_SQL = """ insert into log
			(phrase, letters, ip, browser_string, results)
			values
			(%s, %s, %s, %s, %s)"""
		cursor.execute(_SQL, (	req.form['phrase'],
				req.form['letters'],
				req.remote_addr,
				req.user_agent.browser,
				res,)
		)


""" This is our older function implementation
@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)
"""

@app.route('/viewlog')
def view_the_log() -> 'html':
	try:
		with UseDatabase(app.config['dbconfig']) as cursor:
			_SQL = """ select phrase, letters, ip, browser_string, results from log"""
			cursor.execute(_SQL)
			contents = cursor.fetchall()
			titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
			return render_template(	'viewlog.html',
					the_title='View Log',
					the_row_titles=titles,
					the_data=contents,
			)
	except mysql.connector.erros.InterfaceError as err:
		print('Is your database switched on ? Error: ', str(err))
	except Exception as err:
		print('Something went wrong', str(err))

if __name__ == '__main__':
    app.run(debug=True)
