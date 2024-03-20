from flask import Flask, render_template, request
import httpretty
import json
import mysql.connector
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='トップページ')

@app.route('/analyze', methods=['POST'])
def analyze():
	# APIのmock-upを有効化
	enable_mock(enabled=True, is_success=True)

	# APIリクエスト
	URL = "http://example.com/"
	image_path = request.form.get("image_path")
	data = {"image_path": image_path}
	request_timestamp = int(time.time())
	response = requests.post(URL, data=data)
	response_timestamp = int(time.time())
	image_info = response.json()

	# APIのmock-upを無効化
	if httpretty.is_enabled():
		httpretty.disable()
		httpretty.reset()

	# MySQL接続
	cnx = mysql.connector.connect(
		host="localhost",
		user="root",
		database="invox"
	)
	cursor = cnx.cursor()

	# データ挿入
	query = get_query()
	insert_value = get_insert_value(
		image_path, 
		image_info, 
		request_timestamp, 
		response_timestamp)
	cursor.execute(query, insert_value)
	cnx.commit()

	# MySQL接続を閉じる
	cursor.close()
	cnx.close()

	return render_template('result.html', title='結果ページ')

def enable_mock(enabled, is_success):
	if not enabled:
		# mock-upを有効化しない
		return

	httpretty.enable(verbose=True, allow_net_connect=True)
	if is_success:
		# リクエスト成功時のデータ
		dummy = {
			"success": "true", 
			"message": "success", 
			"estimated_data": {"class": 3, "confidence": 0.8683}, 
		}
	else:
		# リクエスト失敗時のデータ
		dummy = {
			"success": "false", 
			"message": "Error:E50012", 
			"estimated_data": {}, 
		}
	httpretty.register_uri(
		httpretty.POST, 
		"http://example.com/", 
		body=json.dumps(dummy))

def get_query():	
	query = \
		'INSERT INTO ai_analysis_log ('\
			'image_path, '\
			'success, '\
			'message, '\
			'class, '\
			'confidence, '\
			'request_timestamp, '\
			'response_timestamp) '\
		'VALUES ('\
			'%(image_path)s, '\
			'%(success)s, '\
			'%(message)s, '\
			'%(class)s, '\
			'%(confidence)s, '\
			'%(request_timestamp)s, '\
			'%(response_timestamp)s)'
	return query

def get_insert_value(image_path, image_info, request_timestamp, response_timestamp):
	success = image_info.get("success")
	message = image_info.get("message")
	estimated_data = image_info.get("estimated_data")
	if estimated_data:
		class_ = estimated_data.get("class")
		confidence = estimated_data.get("confidence")
	else:
		class_ = None
		confidence = None

	insert_value = {
		"image_path": image_path, 
		"success": success, 
		"message": message, 
		"class": class_, 
		"confidence": confidence, 
		"request_timestamp": request_timestamp, 
		"response_timestamp": response_timestamp, 
	}
	return insert_value

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
