from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

"""Создаем список чтобы не использовать базы данных"""
ads = []


"""Функция создания объявлений"""
@app.route('/ads', methods=['POST'])
def create_ad():
    data = request.get_json()
    current_time = datetime.now()
    new_ad = {'title': data['title'], 'description': data['description'], 'creation_date': current_time, 'owner': data['owner']}
    ads.append(new_ad)
    return jsonify({'ad': new_ad})


"""Функция получения объявлений"""
@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    for ad in ads:
        if ad['id'] == ad_id:
            return jsonify({'ad': ad})
        return jsonify({'error': 'Ad not found'})


"""Функция получения объявлений"""
@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    for ad in ads:
        if ad['id'] == ad_id:
            ads.remove(ad)
            return jsonify({'message': 'Ad deleted successfully'})
        return jsonify({'error': 'Ad not found'})


if __name__ == 'main':
    app.run(debug=True)