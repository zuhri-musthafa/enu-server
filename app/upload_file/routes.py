from flask import Blueprint, request, jsonify
import csv
from io import TextIOWrapper
from app.data_penerima.models import DataPenerima
from app import db

upload_file_bp = Blueprint('upload', __name__, url_prefix='/api')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['csv']


def process_csv(file):
    file_stream = TextIOWrapper(file, encoding='utf-8')
    csv_reader = csv.DictReader(file_stream)
    data_list = []

    for row in csv_reader:
        existing_data = DataPenerima.query.filter_by(
            nama=row.get('nama')).first()

        if existing_data:
            existing_data.k1 = int(row['Kondisi Keluarga'])
            existing_data.k2 = int(row['Status Pemasukan'])
            existing_data.k3 = int(row['Status Pekerjaan'])
            existing_data.k4 = int(row['Jumlah Tanggungan'])
            existing_data.k5 = int(row['Kondisi Kesehatan'])
            existing_data.k6 = int(row['Kondisi Tempat Tinggal'])
            existing_data.k7 = int(row['Status Tempat Tinggal'])
        else:
            new_data = DataPenerima(
                nama=row['nama'],
                k1=int(row['Kondisi Keluarga']),
                k2=int(row['Status Pemasukan']),
                k3=int(row['Status Pekerjaan']),
                k4=int(row['Jumlah Tanggungan']),
                k5=int(row['Kondisi Kesehatan']),
                k6=int(row['Kondisi Tempat Tinggal']),
                k7=int(row['Status Tempat Tinggal'])
            )
            db.session.add(new_data)

    db.session.commit()


@upload_file_bp.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        process_csv(file)
        return jsonify({'message': 'File uploaded successfully'}), 201
    else:
        return jsonify({'message': 'Invalid file type'}), 400
