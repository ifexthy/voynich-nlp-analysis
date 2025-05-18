import json
import os
import re
import csv
from docx import Document

# === Configuration ===
voynich_doc_path = './data/AB.docx'
cluster_json_path = './data/stripped_cluster_lookup.json'
output_csv_path = './results/voynich_line_clusters.csv'
suffixes = ['aiin', 'dy', 'in', 'chy', 'chey', 'edy', 'ey', 'y']

# === Load stripped word → cluster ID mapping ===
if os.path.exists(cluster_json_path):
    with open(cluster_json_path, 'r') as f:
        cluster_lookup = json.load(f)
else:
    raise FileNotFoundError("Cluster JSON file not found. Please run the SBERT script to generate it.")

# === Function to strip suffixes ===
def strip_suffix(word):
    for suffix in sorted(suffixes, key=len, reverse=True):
        if word.endswith(suffix):
            return re.sub(f'{suffix}$', '', word)
    return word

# === Parse the Voynich Word document ===
document = Document(voynich_doc_path)
cluster_lines = []

for para in document.paragraphs:
    text = para.text.strip()
    if not text or not text.startswith('<'):
        continue

    parts = text.split()
    tag = parts[0]
    words = parts[1:]

    stripped = [strip_suffix(word) for word in words]
    clusters = [cluster_lookup.get(word, None) for word in stripped]

    cluster_lines.append((tag, clusters))

# === Write output to CSV ===
with open(output_csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Line Tag", "Cluster Sequence"])
    for tag, clusters in cluster_lines:
        writer.writerow([tag, clusters])

output_csv_path
