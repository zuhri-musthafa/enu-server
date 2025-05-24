from flask import Blueprint, request, jsonify
from app.data_penerima.models import DataPenerima
from app import db
import pandas as pd
from sklearn.cluster import KMeans

cluster_bp = Blueprint('cluster', __name__, url_prefix='/api')


def cluster_data(n_clusters=2):
    # Ambil data dari database
    data = DataPenerima.query.with_entities(
        DataPenerima.id, DataPenerima.k1, DataPenerima.k2, DataPenerima.k3,
        DataPenerima.k4, DataPenerima.k5, DataPenerima.k6, DataPenerima.k7
    ).all()

    if not data:
        return {'message': 'No data available for clustering'}, 400

    # Simpan ID dalam list terpisah
    ids = [int(row.id) for row in data]

    # Konversi ke DataFrame tanpa kolom ID
    df = pd.DataFrame(
        [[row.k1, row.k2, row.k3, row.k4, row.k5, row.k6, row.k7]
            for row in data],
        columns=['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']
    )

    # Menjalankan K-Means
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42, n_init=50)
    clusters = kmeans.fit_predict(df)

    # Memperbarui database dengan hasil clustering
    for i, cluster_label in enumerate(clusters):
        data_penerima = DataPenerima.query.get(ids[i])
        data_penerima.cluster = int(cluster_label)

    db.session.commit()

    return f"Clustering completed with {n_clusters} clusters"


@cluster_bp.route('/cluster', methods=['POST'])
def run_clustering():
    try:
        n_clusters = request.json.get('n_clusters', 2)
        result = cluster_data(n_clusters)
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': 'Error in clustering', 'error': str(e)}), 500

