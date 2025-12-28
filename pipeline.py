import pathway as pw
from pathway.stdlib.indexing import KNNIndex

class DocumentSchema(pw.Schema):
    text: str

# Read documents LIVE from folder
documents = pw.io.fs.read(
    "./data",
    format="text",
    schema=DocumentSchema,
    with_metadata=True
)

# Create live vector index
index = KNNIndex(
    documents.text,
    documents,
)

print("✅ Pathway pipeline started. Watching documents...")

pw.run()
