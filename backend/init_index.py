from opensearchpy import OpenSearch  
client = OpenSearch('http://localhost:9200')  
mapping = {  
  "mappings": {  
    "properties": {  
      "@timestamp": {"type": "date", "format": "strict_date_optional_time||epoch_millis"},  
      "tenant": {"type": "keyword"},  
      "source": {"type": "keyword"},  
      "vendor": {"type": "keyword"},  
      "product": {"type": "keyword"},  
      "event_type": {"type": "keyword"},  
      "event_subtype": {"type": "keyword"},  
      "severity": {"type": "integer"},  
      "action": {"type": "keyword"},  
      "src_ip": {"type": "ip"},  
      "src_port": {"type": "integer"},  
      "dst_ip": {"type": "ip"},  
      "dst_port": {"type": "integer"},  
      "protocol": {"type": "keyword"},  
      "user": {"type": "keyword"},  
      "host": {"type": "keyword"},  
      "process": {"type": "keyword"},  
      "url": {"type": "keyword"},  
      "http_method": {"type": "keyword"},  
      "status_code": {"type": "integer"},  
      "rule_name": {"type": "keyword"},  
      "rule_id": {"type": "keyword"},  
      "cloud.account_id": {"type": "keyword"},  
      "cloud.region": {"type": "keyword"},  
      "cloud.service": {"type": "keyword"},  
      "raw": {"type": "text"},  
      "_tags": {"type": "keyword"},  
      "geo": {"type": "object"}  
    }  
  }  
}  
#client.indices.create(index='logs-*', body=mapping)
index_name = 'logs-general'
#สร้าง index ใหม่
try:
    client.indices.put_settings(index="_all", body={
        "index.blocks.read_only_allow_delete": None
    })
except Exception as e:
    print(f"Note: Could not clear read-only block: {e}")

# 2. เช็คว่ามี Index อยู่แล้วหรือไม่
if client.indices.exists(index=index_name):
    print(f"Index '{index_name}' already exists. Skipping creation.")
else:
    # 3. ถ้ายังไม่มี ให้สร้างใหม่
    try:
        response = client.indices.create(index=index_name, body=mapping)
        print(f"Create Index Response: {response}")
    except Exception as e:
        print(f"Failed to create index: {e}")

# 4. ตรวจสอบสถานะ
try:
    current_mapping = client.indices.get_mapping(index=index_name)
    print("\n--- Current Mapping in OpenSearch ---")
    print(current_mapping)
except Exception as e:
    print(f"Could not get mapping: {e}")