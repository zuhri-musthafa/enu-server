from flask import Blueprint, request, jsonify
from app.data_penerima.models import DataPenerima
from app import db

data_penerima_bp = Blueprint('data_penerima', __name__, url_prefix='/api')

# Create data penerima


@data_penerima_bp.route('/data_penerima', methods=['POST'])
def create_data_penerima():
    request_form = request.get_json()
    new_data_penerima = DataPenerima(
        nama=request_form['nama'],
        k1=request_form['k1'],
        k2=request_form['k2'],
        k3=request_form['k3'],
        k4=request_form['k4'],
        k5=request_form['k5'],
        k6=request_form['k6'],
        k7=request_form['k7']
    )

    db.session.add(new_data_penerima)
    db.session.commit()

    response = DataPenerima.query.get(new_data_penerima.id).to_dict()
    return jsonify(response)

# Read data penerima


@data_penerima_bp.route('/data_penerima', methods=['GET'])
def get_data_penerima():
    cluster = request.args.get('cluster', type=int)
    query = DataPenerima.query
    if cluster is not None:
        query = query.filter_by(cluster=cluster)

    data_penerima = DataPenerima.query.all()
    response = []
    for data in data_penerima:
        response.append(data.to_dict())
    return jsonify(response)

# Read data penerima by id


@data_penerima_bp.route('/data_penerima/<int:id>', methods=['GET'])
def get_data_penerima_by_id(id):
    data_penerima = DataPenerima.query.get(id)
    response = data_penerima.to_dict()
    return jsonify(response)

# Update data penerima


@data_penerima_bp.route('/data_penerima/<int:id>', methods=['PUT'])
def update_data_penerima(id):
    data_penerima = DataPenerima.query.get(id)
    request_form = request.get_json()

    data_penerima.nama = request_form['nama']
    data_penerima.k1 = request_form['k1']
    data_penerima.k2 = request_form['k2']
    data_penerima.k3 = request_form['k3']
    data_penerima.k4 = request_form['k4']
    data_penerima.k5 = request_form['k5']
    data_penerima.k6 = request_form['k6']
    data_penerima.k7 = request_form['k7']
    data_penerima.cluster = request_form['cluster']

    db.session.commit()

    response = DataPenerima.query.get(data_penerima.id).to_dict()
    return jsonify(response)

# Delete data penerima


@data_penerima_bp.route('/data_penerima/<int:id>', methods=['DELETE'])
def delete_data_penerima(id):
    DataPenerima.query.filter_by(id=id).delete()
    db.session.commit()

    return ('Data Penerima dengan id "{}" berhasil dihapus'.format(id), 200)
